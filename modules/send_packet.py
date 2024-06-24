import json
import struct
import socket
from PySide6.QtWidgets import QMessageBox
from modules.util import *

class SendPacket:
    def __init__(self, main_window):
        self.main_window = main_window
        self.page = 1
        
    def connectSocket(self, addr, port):
        try:
            print(f"Connecting to {addr}:{port}")
            self.main_window.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.main_window.socket.settimeout(5)
            self.main_window.socket.connect((addr, port))
            self.main_window.socket.setblocking(False)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def loginRequest(self, socket):
        # self.loginId = self.main_window.login_input_id.text()
        # loginPw = self.main_window.login_input_pw.text()
        self.loginId = "login_id1"
        loginPw = "password1"
        try:
            msg = {
                "type": TYPE_LOGIN,
                "login_id": self.loginId,
                "pw": loginPw
            }
            packet = jsonParser(msg)

            if socket and msg:
                socket.sendall(packet)

            self.main_window.btn_home.show()
            self.main_window.btn_admin.show()
            self.main_window.btn_notice.show()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def qrLoginRequest(self, socket, msg):
        try:
            packet = jsonParser(msg)

            if socket and msg:
                socket.sendall(packet)

            self.main_window.btn_home.show()
            self.main_window.btn_admin.show()
            self.main_window.btn_notice.show()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        
    def signUpRequest(self, socket):
        self.signupId = self.main_window.signup_input_id.text()
        self.signupPw = self.main_window.signup_input_pw.text()
        self.signupName = self.main_window.signup_input_name.text()
        self.signupPhone = self.main_window.signup_input_phone.text()
        self.signupEmail = self.main_window.signup_input_email.text()
        self.signupDept = self.main_window.signup_combo_dept.currentText()
        self.signupPosition = self.main_window.signup_combo_position.currentText()
        
        try:
            # msg = {"type": 1,
            #             "id": self.signupId, 
            #             "pw": self.signupPw,
            #             "name": self.signupName,
            #             "phone": self.signupPhone,
            #             "email": self.signupEmail,
            #             "dept": self.signupDept,
            #             "pos": self.signupPosition}
            msg = {"type": 1,
                        "login_id": "login_id26", 
                        "pw": "password26",
                        "name": "아이디이십육",
                        "phone": "010-1234-9653",
                        "email": "eluon@gmail.com"}
            packet = jsonParser(msg)
            
            print(packet)
        
            if socket and msg:
                socket.sendall(packet)
            
            # QMessageBox.information(self.main_window, "SignUp", "id: " + self.signupId + '\n'
            #                                     "pw: " + self.signupPw + '\n'
            #                                     "name: " + self.signupName + '\n'
            #                                     "Phone: " + self.signupPhone + '\n'
            #                                     "Email: " + self.signupEmail + '\n'
            #                                     "Dept: " + self.signupDept + '\n'
            #                                     "Position: " + self.signupPosition + '\n')
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def sendMsg(self, socket):
        self.msgText = self.main_window.home_lineedit_chatlist_send.text()
        self.loginId = "eluon"
        self.groupName = "채팅방 1"
        try:
            msg = {"type": TYPE_MESSAGE,
                   "login_id": self.loginId,
                   "groupname": self.groupName,
                   "text": self.msgText}
            
            packet = jsonParser(msg)
        
            if socket and msg:
                socket.sendall(packet)
                
            self.main_window.updateMsgDisplay(self.msgText, "sent")
            
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def reqUserList(self, socket):
        try:
            msg = {"type": TYPE_USERLIST,
                    "page": self.page}
            print("요청된 페이지")
            print(self.page)
            packet = jsonParser(msg)
        
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def reqGroupList(self, socket):
        try:
            msg = {"type": TYPE_GROUPLIST}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            print("메세지 보냄")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def reqAddGroupMember(self, socket, groupname, userlist):
        try:
            msg = {
	                "type": 7,
	                "groupname": groupname,
	                "login_id" : userlist}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            print(msg)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def reqGroupMemberList(self, socket, groupname):
        msg = {
                "type": 11,
                "groupname": groupname
        }
        if msg["groupname"]==None:
            QMessageBox.warning(self.main_window, 'Warning', '그룹을 선택해주세요')
            raise Exception('그룹을 선택해주세요')
        packet = jsonParser(msg)
        if socket and msg:
            socket.sendall(packet)
        print(msg)
    
    def testDataSender(self, socket):
        print("type: 11 보냄")
        try:
            msg = {"type": 7,
                   "groupname": "groupname1",
                   "login_id":["login_id2", "login_id3", "login_id4"]}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            print(msg)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def printSendClass(self):
        print("어쨌든 SendPacketClass 불러냈음")
            
        
def jsonParser(msg):
    json_msg = json.dumps(msg, ensure_ascii=False)
    byte_json_msg = bytes(json_msg, 'utf-8')
    msg_length = len(byte_json_msg)
    total_length = msg_length + 4
    header = struct.pack('<I', total_length)
    
    return header + byte_json_msg