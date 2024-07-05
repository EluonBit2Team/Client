import json
import struct
import select
import threading
import time
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
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.receivedPacket = 0
        self.running = True
        self.messageSignal.connect(self.main_window.alertMsgBox)
        self.loginSignal.connect(self.main_window.setGUILoginSucess)

    def receiveData(self, socket):
        self.sock = socket
        buffer = b""
        start_time = time.time()
        while self.running:
            try:
                if self.sock:
                    readable, _, _ = select.select([self.sock], [], [], 0.5)
                    if readable:
                        data = self.sock.recv(4096)
                        if data:
                            start_time = time.time()
                            buffer += data
                            print("-------받은 RAW DATA--------")
                            print(data)
                            print("---------------------------")
                            while len(buffer) >= 4:
                                msg_length = struct.unpack('<I', buffer[:4])[0]
                                print(msg_length)
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:msg_length]
                                    buffer = buffer[msg_length:]
                                    json_type = json.loads(json_msg).get("type")
                                    self.receivedType(json_type, json_msg)
                                else:
                                    print("데이터가 없습니다")
                                    break
                    # if time.time() - start_time > 4: 
                    #     print("Timeout: No data received for 4 seconds. Closing socket.")
                    #     self.main_window.packetSender.ping_flag = False
                    #     self.main_window.packetSender.disconnect()
                    #     break
            except BlockingIOError:
                continue
            except Exception as e:
                self.main_window.setLoginPage()
                # self.main_window.login_btn_reconnect.show()
                # self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.loginpage)
                print(f"An error occurred: {e}")
                self.running = False
                self.main_window.isConnect = False
                print("receive가 끊어졌습니다")
            # except BlockingIOError:
            #     continue
            # except (OSError, self.socket.error) as e: #좀더 자세한 소켓연결 오류와 라인을 알고싶을때
            #     print(f"An error occurred: {e}")
            #     self.running = False
            #     buffer = b""
            #     break
            # except Exception as e:
            #     print(f"An unexpected error occurred: {e}")
            #     self.running = False
            #     break
    
    def connectSuccess(self, msg):
        self.main_window.isConnect = True
            
    def loginSuccess(self, msg):
        userId = json.loads(msg.decode('utf-8')).get("login_id")
        userRole = json.loads(msg.decode('utf-8')).get("role")
        print("로그인 성공")
        print("id: " + userId)
        print("직급: " + str(userRole))
        self.main_window.userId = userId
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
        self.loginSignal.emit(userId)
        
        # if userRole == 1:
        #     self.main_window.ui.btn_admin.show()
        #     self.main_window.ui.btn_notice.show()
        
    def receiveMassage(self, msg):
        receivedMessage = json.loads(msg.decode('utf-8'))
        recvGroupName = json.loads(msg.decode('utf-8')).get("groupname")
        if recvGroupName == self.main_window.nowGroupName:
            updateDisplay(self.main_window, receivedMessage, "receivedChat", self.main_window.chatListModel)
        else:
            print("잘못된 그룹")
            return False
    
    def receivedDm(self, msg):
        dm = json.loads(msg.decode('utf-8'))
        sender = dm['sender_login_id']
        receiver = dm['recver_login_id']
        
        if self.main_window.userId == sender or self.main_window.userId == receiver:
            updateDisplay(self.main_window, dm, "receivedDm", self.main_window.chatListModel)
        else:
            print("다른 개인메세지로 연결되었습니다.")
    
    def receiveUserList(self, msg):
        userList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("users")
        updateDisplay(self.main_window, userList, "userlist", self.main_window.userListModel)
    
    def receiveGroupList(self, msg):
        self.groupList = json.loads(msg.decode('utf-8')).get("groups")
        updateDisplay(self.main_window, self.groupList, "grouplist", self.main_window.groupListModel)
    
    def receiveGroupMember(self, msg):
        groupMemberList = json.loads(msg.decode('utf-8')).get("users")
        updateDisplay(self.main_window, groupMemberList, "groupMemberList", self.main_window.groupMember.groupMemberModel)
        updateDisplay(self.main_window, groupMemberList, "groupMemberList", self.main_window.memberAddDialog.treeview_right_model)

    def receiveReqList(self, msg):
        signupList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("signup_req_list")
        groupReqList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("group_req_list")
        reqList = signupList + groupReqList
        print (reqList)
        if reqList:
            updateDisplay(self.main_window, reqList, "reqList", self.main_window.adminReqListModel)
        else:
            self.main_window.adminReqListModel.clear()
    
    def receiveGroupChat(self, msg):
        receivedMessage = json.loads(msg.decode('utf-8'))
        recvGroupName = receivedMessage.get("groupname")
        if recvGroupName == self.main_window.nowGroupName:
            updateDisplay(self.main_window, receivedMessage.get("chatlog"), "clickedGroup", self.main_window.chatListModel)
            
    def receiveDmLog(self, msg):
        dm = json.loads(msg.decode('utf-8'))
        updateDisplay(self.main_window, dm.get("dmlog"), "clickedUser", self.main_window.chatListModel)
        
    # 로그
    def receiveReqLogList(self, msg):
        print("receiveReqLogList 진입")
        serverLogList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("server_log_list")
        if serverLogList:
            print("if문 serverLogList 진입")
            updateDisplay(self.main_window, serverLogList, "serverLogList", self.main_window.logReqListModel)
        else:
            self.main_window.logReqListModel.clear()
    
    # 사용자 로그
    def receiveReqUserLogList(self, msg):
        print("receiveReqUserLogList 진입")
        userLogList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("user_log_list")
        if userLogList:
            print("if문 userLogList 진입")
            updateDisplay(self.main_window, userLogList, "userLogList", self.main_window.loguserReqListModel)
        else:
            self.main_window.loguserReqListModel.clear()

    # type 300
    def onlineReq(self, msg):
        self.main_window.admin_label_new.show()
        print("onlineReq 진입")
        print(msg)

        # if not self.main_window.admin_label_new.show():
        #     self.main_window.admin_label_new.show()

   
    # type 301 (서버 종료)
    def serverErrorReq(self, msg):
        print("301 표출 (서버 오류)")
        print(msg)

        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.loginpage)
        self.main_window.packetSender.disconnect()
        print("소켓 종료")
        # # 경고 다이얼로그 추가
        # msgBox = QMessageBox()
        # msgBox.setIcon(QMessageBox.Warning)
        # msgBox.setText("서버 오류가 발생했습니다. 다시 시도해 주세요.")
        # msgBox.setWindowTitle("서버 오류")
        # msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.exec_()
                
        
    # 실시간
    def receiveReqRealtime(self, msg):
        try:
            print("receiveReqRealtime 진입")
            decoded_msg = msg.decode('utf-8')
            parsed_json = json.loads(decoded_msg, object_pairs_hook=OrderedDict)

            realtimememList = parsed_json.get("mem")
            realtimeloginList = parsed_json.get("login_user_cnt")
            realtimetpsList = parsed_json.get("tps")

            print(f"realtimememList: {realtimememList}")
            print(f"realtimeloginList: {realtimeloginList}")
            print(f"realtimetpsList: {realtimetpsList}")

            if realtimememList is not None:
                print("if문 realtimememList 진입")
                updateDisplay(self.main_window, [realtimememList], "realtimememList", self.main_window.realtimememListModel)
            if realtimeloginList is not None:
                print("if문 realtimeloginList 진입")
                updateDisplay(self.main_window, [realtimeloginList], "realtimeloginList", self.main_window.realtimeloginListModel)
            if realtimetpsList is not None:
                print("if문 realtimetpsList 진입")
                updateDisplay(self.main_window, [realtimetpsList], "realtimetpsList", self.main_window.realtimetpsListModel)
            if realtimememList is None and realtimeloginList is None and realtimetpsList is None:
                print("else문 진입 - 모든 모델을 클리어합니다.")
                self.main_window.realtimememListModel.clear()
                self.main_window.realtimeloginListModel.clear()
                self.main_window.realtimetpsListModel.clear()
        except Exception as e:
            print(f"예외 발생: {e}")
    
    def loginError(self, msg):
        errorMsg = msg
        alertMsg = "중복된 아이디 입니다."
        self.main_window.alertMsg = alertMsg
        self.messageSignal.emit(alertMsg)
    
    def receiveLoginUser(self, msg):
        users = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("current_user_list")
        self.main_window.loginUserList.clear()
        for json_data in users:
            self.main_window.loginUserList.append(json_data['login_id'])
        
        
        
        
    def receiveError(self, msg):
        errorMsg = json.loads(msg.decode('utf-8')).get("msg")
        print(errorMsg)
        
    def receivedType(self, jsonType, msg):
        if jsonType == TYPE_LOGIN:
            self.loginSuccess(msg)
        elif jsonType == TYPE_CONNECTION:
            self.connectSuccess(msg)
        elif jsonType == TYPE_USERLIST:
            self.receiveUserList(msg)
        elif jsonType == TYPE_MESSAGE:
            self.receiveMassage(msg)
        elif jsonType == TYPE_ERROR:
            self.receiveError(msg)
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
            self.loginError(msg)
        elif jsonType == TYPE_ONLINE_REQ:
            self.onlineReq(msg)
        elif jsonType == TYPE_SERVERERR_REQ:
            self.serverErrorReq(msg)
        elif jsonType == TYPE_CURRENT_USERLIST:
            self.receiveLoginUser(msg)
        else:
            print("jsonType이 None입니다.")
            print("------NoneType RAW DATA ------")
            print(msg)
            print("------------------------------")
            