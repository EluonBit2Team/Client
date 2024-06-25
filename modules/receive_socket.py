import json
import struct
import select
import threading
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
                        print(data)
                        if data:
                            print(buffer)
                            buffer += data
                            while len(buffer) >= 4:
                                msg_length = struct.unpack('<I', buffer[:4])[0]
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:4 + msg_length]
                                    buffer = buffer[4 + msg_length:]
                                    json_type = json.loads(json_msg).get("type")
                                    self.receivedType(json_type, json_msg)
                                else:
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
        print("로그인 성공")
        print("id: " + userId)
        self.main_window.userId = userId
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
        #ishost
        # self.main_window.packetSender.reqAcceptList(self.main_window.socket)
        # self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.home)
        
    def receiveMassage(self, msg):
        receivedMessage = json.loads(msg.decode('utf-8')).get("text")
        updateDisplay(self.main_window, receivedMessage, "received", self.main_window.chatListModel)
    
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
        # self.main_window.groupMember.updateDisplay(groupMemberList, self.main_window.groupMember.groupMemberModel)
    
    def receiveReqList(self, msg):
        print("receiveReqList 호출")
        signupList = json.loads(msg.decode('utf-8')).get("signup_req_list")
        print(signupList)
        groupReqList = json.loads(msg.decode('utf-8')).get("group_req_list")
        if signupList:
            updateDisplay(self.main_window, signupList, "signupList", self.main_window.adminReqListModel)
        if groupReqList:
            updateDisplay(self.main_window, groupReqList, "groupReqList", self.main_window.adminReqListModel)
            
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
        else:
            print("jsonType이 None입니다.")
            print("--------- RAW DATA ---------")
            print(msg)
            print("----------------------------")
            