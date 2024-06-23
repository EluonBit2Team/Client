import json
import struct
import select
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
                            print(data)
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
    
    def loginSuccess(self, msg):
        print(msg)
        userId = json.loads(msg.decode('utf-8')).get("id")
        print("로그인 성공")
        print("id: " + userId)
        self.main_window.userId = userId
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
    
    def receiveMassage(self, msg):
        self.receivedMessage = json.loads(msg.decode('utf-8')).get("text")
        print("receivedMessage = " + self.receivedMessage)
        self.main_window.updateMsgDisplay(self.receivedMessage, "received")
    
    def receiveUserList(self, msg):
        userList = json.loads(msg.decode('utf-8')).get("users")
        self.main_window.updateDisplay(userList, "userlist", self.main_window.userListModel)
    
    def receiveGroupList(self, msg):
        self.groupList = json.loads(msg.decode('utf-8')).get("groups")
        print(msg)
        self.main_window.updateDisplay(self.groupList, "grouplist", self.main_window.groupListModel)
    
    def receiveGroupMember(self, msg):
        groupMemberList = json.loads(msg.decode('utf-8')).get("users")
        print(groupMemberList)
        self.main_window.groupMember.updateDisplay(groupMemberList, self.main_window.groupMember.groupMemberModel)
        
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
            print(msg)
            self.receiveGroupMember(msg)
        else:
            print("jsonType이 None입니다.")
            print("--------- RAW DATA ---------")
            print(msg)
            print("----------------------------")
            