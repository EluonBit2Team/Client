import json
import struct
import select
import threading
from datetime import datetime
from collections import OrderedDict
from PySide6.QtWidgets import QMessageBox
from modules.util import *
from modules.send_packet import *


class ReceivePacket():
    def __init__(self, main_window):
        self.main_window = main_window
        self.receivedPacket = 0
        self.running = True
        

    def receiveData(self, socket):
        self.sock = socket
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
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:msg_length]
                                    buffer = buffer[msg_length:]
                                    
                                    json_type = json.loads(json_msg).get("type")
                                    self.receivedType(json_type, json_msg)
                                else:
                                    print("데이터가 없습니다")
                                    break
            except BlockingIOError:
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False
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
            
    
    def loginSuccess(self, msg):
        print(msg)
        userId = json.loads(msg.decode('utf-8')).get("login_id")
        userRole = json.loads(msg.decode('utf-8')).get("role")
        print("로그인 성공")
        print("id: " + userId)
        print("직급: " + str(userRole))
        self.main_window.userId = userId
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
        
        self.main_window.ui.btn_login.hide()
        print("lself.main_window.ui.btn_login.hide() 성공")
        
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
        
    
    def receiveUserList(self, msg):
        userList = json.loads(msg.decode('utf-8')).get("users")
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
        
    
    def receiveReqLogList(self, msg):
        print("receiveReqLogList 진입")
        serverLogList = json.loads(msg.decode('utf-8'), object_pairs_hook=OrderedDict).get("server_log_list")
        if serverLogList:
            print("if문 serverLogList 진입")
            updateDisplay(self.main_window, serverLogList, "serverLogList", self.main_window.logReqListModel)
        else:
            self.main_window.logReqListModel.clear()

    def receiveError(self, msg):
        errorMsg = json.loads(msg.decode('utf-8')).get("msg")
        print(errorMsg)
        
    def receivedType(self, jsonType, msg):
        if jsonType == TYPE_LOGIN:
            self.loginSuccess(msg)
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
        # elfi jsonType == 
        else:
            print("jsonType이 None입니다.")
            print("------NoneType RAW DATA ------")
            print(msg)
            print("------------------------------")
            