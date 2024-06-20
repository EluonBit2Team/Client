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
                            print("--------- RAW DATA ---------")
                            print(data)
                            print("----------------------------")
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
        successMsg = json.loads(msg.decode('utf-8')).get("msg")
        userId = json.loads(msg.decode('utf-8')).get("id")
        print(successMsg)
        print("id: " + userId)
        self.main_window.userId = userId
        self.main_window.packetSender.reqGroupList(self.main_window.socket)
        self.main_window.packetSender.reqUserList(self.main_window.socket)
    
    def receiveMassage(self, msg):
        self.receivedMessage = json.loads(msg.decode('utf-8')).get("text")
        print("receivedMessage = " + self.receivedMessage)
        self.main_window.updateMsgDisplay(self.receivedMessage, "received")
    
    def receiveUserList(self, msg):
        print(msg)
        userList = json.loads(msg.decode('utf-8')).get("users")
        print(userList)
        self.main_window.updateDisplay(userList, "userlist")
    
    def receiveGroupList(self, msg):
        self.groupList = json.loads(msg.decode('utf-8')).get("groups")
        print(self.groupList)
        self.main_window.updateDisplay(self.groupList, "grouplist")
        
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
        else:
            print("jsonType이 None입니다.")
            