import json
import struct
import select
from PySide6.QtWidgets import QMessageBox
from modules.util import *

TYPE_LOGIN = 101
TYPE_MESSAGE = 0
TYPE_USERLIST = 5
TYPE_ERROR = 100

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
                                    # self.message = json.loads(json_msg.decode('utf-8')).get("text")
                                    # self.main_window.updateMsgDisplay(self.message, "received")
                                    message_dict = json.loads(json_msg.decode('utf-8'))
                                    type = message_dict.get("type")
                                
                                    if type is not None:
                                        print("타입: " + str(type))
                                        self.receivedType(type, json_msg)
                                        print(json_msg)
                                    else:
                                        print("타입이 없습니다.")
                                else:
                                    break
            except BlockingIOError:
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False
    
    def receiveMassage(self, msg):
        self.receivedMessage = json.loads(msg.decode('utf-8')).get("text")
        print("receivedMessage = " + self.receivedMessage)
        self.main_window.updateMsgDisplay(self.receivedMessage, "received")
    
    def receiveUserList(self, msg):
        print(msg)
        userList = json.loads(msg.decode('utf-8')).get("users")
        print(userList)
    
    def loginSuccess(self, msg):
        print(msg)
        successMsg = json.loads(msg.decode('utf-8')).get("msg")
        print(successMsg)
    
    def receiveError(self, msg):
        errorMsg = json.loads(msg.decode('utf-8')).get("msg")
        print(errorMsg)
        
    def receivedType(self, type, msg):
        self.type = type
        type(self.type)
        print("self.type의 값")
        print(self.type)
        if self.type == TYPE_LOGIN:
            self.receiveMassage(msg)
        elif self.type == TYPE_USERLIST:
            self.receiveUserList(msg)
        elif self.type == TYPE_MESSAGE:
            self.receiveMassage(msg)
        else:
            print("self.type이 None입니다.")
            