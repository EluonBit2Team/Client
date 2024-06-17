import json
import struct
import socket
from PySide6.QtWidgets import QMessageBox
from modules.util import *


class SendPacket:
    def __init__(self, main_window):
        self.main_window = main_window
        
    def connectSocket(self, addr, port):
        try:
            print(f"Connecting to {addr}:{port}")
            self.main_window.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.main_window.socket.settimeout(5)
            self.main_window.socket.connect((addr, port))
            self.main_window.socket.setblocking(False)
            connectionSuccessEvent()
        except socket.error as e:
            print(f"Socket connection error: {e}")
            connectionErrorEvent()

    # def loginRequest(self, socket):
    #     self.sock = socket
    #     loginId = self.main_window.login_input_id.text()
    #     loginPw = self.main_window.login_input_pw.text()
    #     try:
    #         msg = {
    #             "type": 2,
    #             "id": loginId,
    #             "pw": loginPw
    #         }
    #         json_msg = json.dumps(msg, ensure_ascii=False)
    #         byte_json_msg = bytes(json_msg, 'utf-8')
    #         msg_length = len(byte_json_msg)
    #         total_length = msg_length + 4
    #         header = struct.pack('<I', total_length)

    #         if self.sock and msg:
    #             self.sock.sendall(header + json_msg.encode('utf-8'))
    #         print(total_length)
    #         print(json_msg)

    #         # QMessageBox.information(
    #         #     self.main_window, "보낸정보", f"id: {loginId}\n pw: {loginPw}\n")

    #         # self.main_window.start_receiving()

    #         self.main_window.btn_home.show()
    #         self.main_window.btn_admin.show()
    #         self.main_window.btn_notice.show()
    #         return True
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return False
    def loginRequest(self, socket):
        self.sock = socket
        loginId = self.main_window.login_input_id.text()
        loginPw = self.main_window.login_input_pw.text()
        try:
            msg = {
                "type": 4,
                "id": "idid2",
                "groupname": "그룹이름",
                "message": "이러저러한 이유로 이러저러한 방을 요청합니다."
            }
            json_msg = json.dumps(msg, ensure_ascii=False)
            byte_json_msg = bytes(json_msg, 'utf-8')
            msg_length = len(byte_json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)

            if self.sock and msg:
                self.sock.sendall(header + json_msg.encode('utf-8'))
            print(total_length)
            print(json_msg)

            # QMessageBox.information(
            #     self.main_window, "보낸정보", f"id: {loginId}\n pw: {loginPw}\n")

            # self.main_window.start_receiving()

            self.main_window.btn_home.show()
            self.main_window.btn_admin.show()
            self.main_window.btn_notice.show()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    
    def signUpRequest(self, socket):
        self.sock = socket
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
                        "id": "idid10", 
                        "pw": "pwpw6",
                        "name": "아이디십",
                        "phone": "폰번",
                        "email": "이메일팔",
                        "dept": "부서",
                        "pos": "직급"}
            packet = jsonParser(msg)
        
            if self.sock and msg:
                self.sock.sendall(packet)
            
            QMessageBox.information(self.main_window, "SignUp", "id: " + self.signupId + '\n'
                                                "pw: " + self.signupPw + '\n'
                                                "name: " + self.signupName + '\n'
                                                "Phone: " + self.signupPhone + '\n'
                                                "Email: " + self.signupEmail + '\n'
                                                "Dept: " + self.signupDept + '\n'
                                                "Position: " + self.signupPosition + '\n')
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def sendMsg(self, socket):
        self.sock = socket
        self.msgText = self.main_window.home_lineedit_chatlist_send.text()
        self.loginId = "eluon"
        self.groupName = "채팅방 1"
        try:
            msg = {"type": 0,
                   "id": self.loginId,
                   "groupname": self.groupName,
                   "text": self.msgText}
            
            packet = jsonParser(msg)
        
            if self.sock and msg:
                self.sock.sendall(packet)
                
            self.main_window.updateMsgDisplay(self.msgText, "sent")
            
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        
        

def jsonParser(msg):
    json_msg = json.dumps(msg, ensure_ascii=False)
    byte_json_msg = bytes(json_msg, 'utf-8')
    msg_length = len(byte_json_msg)
    total_length = msg_length + 4
    header = struct.pack('<I', total_length)
    
    return header + json_msg.encode('utf-8')