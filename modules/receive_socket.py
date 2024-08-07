import json
import struct
import select
from datetime import datetime
from collections import OrderedDict
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QObject, Signal, Slot, Qt
from modules.util import *
from modules.send_packet import *
import tkinter as tk
from tkinter import messagebox
from widgets import *

class ReceivePacket(QObject):
    messageSignal = Signal(str)
    loginSignal = Signal(str)
    updateDisplaySignal = Signal(QObject, dict, str, QStringListModel)
    updateListSignal = Signal(QObject, list, str, QStringListModel)
    messageNotiSignal = Signal(str, QStandardItemModel, QListView)
    dmNotiSignal = Signal(str, QStandardItemModel, QTreeView)
    disconnectSignal = Signal(str)
    notiSignal = Signal(list, list)
    setPageSignal = Signal(QObject)
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.receivedPacket = 0
        self.running = True
        self.messageSignal.connect(self.main_window.alertMsgBox)
        self.loginSignal.connect(self.main_window.setGUILoginSucess)
        self.updateDisplaySignal.connect(updateDisplay) #아직 메인에 초기화는 안해봤음 안되면 메인에 초기화
        self.updateListSignal.connect(updateDisplay)
        self.messageNotiSignal.connect(groupListNoti)
        self.dmNotiSignal.connect(userListNoti)
        self.disconnectSignal.connect(self.main_window.setDisconnect)
        self.notiSignal.connect(self.main_window.updateIcon)
        self.setPageSignal.connect(self.main_window.updatePage)

    def receiveData(self, sock):
        self.sock = sock
        buffer = b""
        while self.running:
            try:
                if self.sock:
                    readable, _, _ = select.select([self.sock], [], [], 0.5)
                    if readable:
                        data = self.sock.recv(4096)
                        if data:
                            buffer += data
                            print("-------받은 RAW DATA--------")
                            print(data)
                            print("---------------------------")
                            while len(buffer) >= 4:
                                msg_length = struct.unpack('<I', buffer[:4])[0]
                                print(f"메시지 길이: {msg_length}")
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:msg_length]
                                    buffer = buffer[msg_length:]
                                    json_type = json.loads(json_msg).get("type")
                                    if json_type is not None:
                                        self.receivedType(json_type, json_msg)
                                    else:
                                        print("type이 None입니다")
                                        print(json_msg)
                                        break
                                else:
                                    print("데이터가 없습니다")
                                    break
            except BlockingIOError as e:
                print(f"BAn error occurred: {e}")
                continue
            except ValueError as e:
                alertMsg = "연결이 끊어졌습니다."
                self.disconnectSignal.emit(alertMsg)
                print(f"An error occurred: {e}")
                self.running = False
                self.main_window.isConnect = False
                print("receive가 끊어졌습니다")
            except IndexError as e:
                print(f"IAn error occurred: {e}")
                continue
            except KeyError as e:
                print(f"An error occurred: {e}")
                continue
            except socket.error as e:
                alertMsg = "연결이 끊어졌습니다."
                self.disconnectSignal.emit(alertMsg)
                print(f"An error occurred: {e}")
                self.running = False
                self.main_window.isConnect = False
                print("receive가 끊어졌습니다")
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
                
    
    def connectSuccess(self, msg):
        self.main_window.isConnect = True
    #TYPE_LOGIN 2
    def loginSuccess(self, msg):
        userId = json.loads(msg.decode('utf-8')).get("login_id")
        userRole = json.loads(msg.decode('utf-8')).get("role")
        print("로그인 성공")
        print("id: " + userId)
        print("직급: " + str(userRole))
        self.main_window.clientSession.loginSession(userId, userRole)
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
        self.main_window.isLogin = True
        self.loginSignal.emit(userId)
    #TYPE_SIGNUP_REQ 1
    def signupReqSucess(self):
        self.setPageSignal.emit(self.main_window.ui.loginpage)
        print("회원가입 신청 성공")
    #TYPE_MESSAGE 3
    def receiveMessage(self, msg):
        receivedMessage = json.loads(msg.decode('utf-8'))
        recvGroupName = json.loads(msg.decode('utf-8')).get("groupname")
        if self.main_window.isLogin and self.main_window.nowGroupName: # 로그인 상태 및 현재 그룹 이름 확인
            first_key = next(iter(self.main_window.nowClickedRow)) # 클릭된 행의 첫번째 키 확인
            if recvGroupName == self.main_window.nowGroupName and first_key == 'groupname': # 수신된 메시지의 그룹 이름과 현재 그룹 이름 비교
                if self.main_window.listMode == "chat":
                    self.updateDisplaySignal.emit(self.main_window, receivedMessage, "receivedChat", self.main_window.chatListModel)
            else:
                self.messageNotiSignal.emit(recvGroupName, self.main_window.groupListModel, self.main_window.home_listview_chatgroup)
                print("다른그룹에서 받은 메세지")
        else:
            self.messageNotiSignal.emit(recvGroupName, self.main_window.groupListModel, self.main_window.home_listview_chatgroup)
            print("다른그룹에서 받은 메세지")
            return
    
    def receivedDm(self, msg):
        dm = json.loads(msg.decode('utf-8'))
        print(dm)
        sender = dm['sender_login_id']
        receiver = dm['recver_login_id']
        print("talkNow 전")
        if self.main_window.nowClickedRow:
            first_key = next(iter(self.main_window.nowClickedRow))
            if first_key == 'groupname':
                self.dmNotiSignal.emit(sender, self.main_window.userListModel, self.main_window.home_treeview_userlist)
                return False
            else:
                talkNow = self.main_window.nowClickedRow['login_id']
                print("현재 대화중인 사람: " + talkNow)
        else:
            self.dmNotiSignal.emit(sender, self.main_window.userListModel, self.main_window.home_treeview_userlist)
            return False
        
        if not sender == talkNow and receiver == self.main_window.userId:
            self.dmNotiSignal.emit(sender, self.main_window.userListModel, self.main_window.home_treeview_userlist)
        
        if sender == self.main_window.userId and receiver == talkNow:
            if self.main_window.listMode == "chat":
                self.updateDisplaySignal.emit(self.main_window, dm, "receivedDm", self.main_window.chatListModel)
        elif sender == talkNow and receiver == self.main_window.userId:
            if self.main_window.listMode == "chat":
                self.updateDisplaySignal.emit(self.main_window, dm, "receivedDm", self.main_window.chatListModel)
    # TYPE_USERLIST 5
    def receiveUserList(self, msg):
        userList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("users")
        filterUserList = {item["login_id"]: item["name"] for item in userList}
        if not self.main_window.userList or not len(self.main_window.userList) == len(filterUserList):
            self.main_window.userList = filterUserList
        self.updateListSignal.emit(self.main_window, userList, "userlist", self.main_window.userListModel)
    
    def receiveGroupList(self, msg):
        self.groupList = json.loads(msg.decode('utf-8')).get("groups")
        self.updateListSignal.emit(self.main_window, self.groupList, "grouplist", self.main_window.groupListModel)
    
    def receiveGroupMember(self, msg):
        groupMemberList = json.loads(msg.decode('utf-8')).get("users")
        self.updateListSignal.emit(self.main_window, groupMemberList, "groupMemberList", self.main_window.groupMember.groupMemberModel)
        self.updateListSignal.emit(self.main_window, groupMemberList, "groupMemberList", self.main_window.memberAddDialog.treeview_right_model)

    def receiveReqList(self, msg):
        signupList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("signup_req_list")
        groupReqList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("group_req_list")
        reqList = signupList + groupReqList
        print (reqList)
        self.updateListSignal.emit(self.main_window, reqList, "reqList", self.main_window.adminReqListModel)
    
    def receiveGroupChat(self, msg):
        receivedMessage = json.loads(msg.decode('utf-8'))
        recvGroupName = receivedMessage.get("groupname")
        if recvGroupName == self.main_window.nowGroupName:
            self.updateListSignal.emit(self.main_window, receivedMessage.get("chatlog"), "clickedGroup", self.main_window.chatListModel)
            
    def receiveDmLog(self, msg):
        dm = json.loads(msg.decode('utf-8'))
        self.updateListSignal.emit(self.main_window, dm.get("dmlog"), "clickedUser", self.main_window.chatListModel)
        
    # 로그
    def receiveReqLogList(self, msg):
        print("receiveReqLogList 진입")
        serverLogList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("server_log_list")
        self.updateListSignal.emit(self.main_window, serverLogList, "serverLogList", self.main_window.logReqListModel)
    
    # 사용자 로그
    def receiveReqUserLogList(self, msg):
        print("receiveReqUserLogList 진입")
        userLogList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("user_log_list")
        self.updateListSignal.emit(self.main_window, userLogList, "userLogList", self.main_window.loguserReqListModel)
    
    def acceptSignup(self):
        alertMsg = "회원가입을 승인했습니다"
        self.messageSignal.emit(alertMsg)
        self.main_window.packetSender.reqAcceptList(self.main_window.socket)
        print("회원가입 승인")
    
    def acceptGroup(self):
        alertMsg = "그룹생성 승인"
        self.messageSignal.emit(alertMsg)
        self.main_window.packetSender.reqAcceptList(self.main_window.socket)
        print("그룹생성 승인")

    # type 300
    def onlineReq(self):
        self.main_window.packetSender.reqOnlineList(self.main_window.socket)
        showIcon = [self.main_window.admin_label_new]
        hideIcon = []
        self.notiSignal.emit(showIcon, hideIcon)
            
   
    # type 301 (서버 종료)
    def serverErrorReq(self, msg):
        alertMsg = "서버가 종료되었습니다."
        self.disconnectSignal.emit(alertMsg)
        print("301 표출 (서버 오류)")
        print(msg)
                
    # 실시간
    def receiveReqRealtime(self, msg):
        try:
            print("receiveReqRealtime 진입")
            parsed_json = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict)
            
            realtimememList = parsed_json.get("mem")
            realtimeloginList = parsed_json.get("login_user_cnt")
            realtimetpsList = parsed_json.get("tps")

            if realtimememList is not None:
                self.updateDisplaySignal.emit(self.main_window, parsed_json, "realtimememList", self.main_window.realtimememListModel)
            if realtimeloginList is not None:
                self.updateDisplaySignal.emit(self.main_window, parsed_json, "realtimeloginList", self.main_window.realtimeloginListModel)
            if realtimetpsList is not None:
                self.updateDisplaySignal.emit(self.main_window, parsed_json, "realtimetpsList", self.main_window.realtimetpsListModel)
            if realtimememList is None and realtimeloginList is None and realtimetpsList is None:
                print("받은데이터 없음")
        except Exception as e:
            print(f"예외 발생: {e}")
    
    def loginError(self):
        alertMsg = "중복된 아이디 입니다."
        self.main_window.alertMsg = alertMsg
        self.messageSignal.emit(alertMsg)
    
    def errorQboxMsg(self, msg):
        self.messageSignal.emit(msg)
    
    def receiveLoginUser(self, msg):
        users = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("current_user_list")
        self.main_window.loginUserList.clear()
        for json_data in users:
            self.main_window.loginUserList.append(json_data['login_id'])
        
        self.main_window.packetSender.reqUserList(self.main_window.socket)
        
    def receiveError(self, msg):
        errorMsg = json.loads(msg.decode('utf-8')).get("msg")
        self.messageSignal.emit(errorMsg)
        
    def receivedType(self, jsonType, msg):
        if jsonType == TYPE_LOGIN:
            self.loginSuccess(msg)
        elif jsonType == TYPE_CONNECTION:
            self.connectSuccess(msg)
        elif jsonType == TYPE_SIGNUP_REQ:
            self.signupReqSucess()
        elif jsonType == TYPE_USERLIST:
            self.receiveUserList(msg)
        elif jsonType == TYPE_MESSAGE:
            self.receiveMessage(msg)
        elif jsonType == TYPE_ERROR:
            self.receiveError(msg)
        elif jsonType == TYPE_ACCEPT_SIGNUP:
            self.acceptSignup()
        elif jsonType == TYPE_ACCEPT_GROUP:
            self.acceptGroup()
        elif jsonType == TYPE_GROUPLIST:
            self.receiveGroupList(msg)
        elif jsonType == TYPE_GROUPMEMBER:
            self.receiveGroupMember(msg)
        elif jsonType == TYPE_REQ_LIST:
            self.receiveReqList(msg)
        elif jsonType == TYPE_GROUP_CHAT_REQ:
            self.receiveGroupChat(msg)
        elif jsonType == TYPE_LOG_REQ:
            self.receiveReqLogList(msg)
        elif jsonType == TYPE_USERLOG_REQ:
            self.receiveReqUserLogList(msg)
        elif jsonType == TYPE_REALTIME_REQ:
            self.receiveReqRealtime(msg)
        elif jsonType == TYPE_DM_SEND:
            self.receivedDm(msg)
        elif jsonType == TYPE_DM_LOG:
            self.receiveDmLog(msg)
        elif jsonType == TYPE_ERROR_DUP_LOGIN:
            self.loginError()
        elif jsonType == TYPE_ONLINE_REQ:
            self.onlineReq()
        elif jsonType == TYPE_SERVERERR_REQ:
            self.serverErrorReq(msg)
        elif jsonType == TYPE_CURRENT_USERLIST:
            self.receiveLoginUser(msg)
        elif jsonType == TYPE_EDIT_USERINFO:
            self.errorQboxMsg("회원정보수정 성공")
        else:
            print("jsonType이 None입니다.")
            print("------NoneType RAW DATA ------")
            print(msg)
            print("------------------------------")
            