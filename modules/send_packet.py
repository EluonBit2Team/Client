import json
import struct
import socket
from PySide6.QtWidgets import QMessageBox
from modules.util import *

class SendPacket:
    def __init__(self, main_window):
        self.main_window = main_window
        
    # def connectSocket(self, addr, port):
    #     try:
    #         print(self.main_window.socket)
    #         self.main_window.socket = None
    #         print(self.main_window.socket)
    #         print(f"Connecting to {addr}:{port}")
    #         self.main_window.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         self.main_window.socket.settimeout(5)
    #         self.main_window.socket.connect((addr, port))
    #         print(self.main_window.socket)
    #         self.main_window.socket.setblocking(False)
    #         return True
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return False
    def connectSocket(self, addr, port):
        try:
            self.socket = None
            print(self.socket)
            print(f"Connecting to {addr}:{port}")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((addr, port))
            print("connectSocket의 socket")
            print(self.socket)
            self.socket.setblocking(False)
            self.main_window.socket = self.socket
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def loginRequest(self):
        # self.loginId = self.main_window.login_input_id.text()
        # loginPw = self.main_window.login_input_pw.text()
        self.socket = self.main_window.socket
        
        if self.socket == None:
            if not self.connectSocket(SERVER_ADDR, SERVER_PORT):
                print("Socket connection failed.")
                socket = self.main_window.socket
                self.main_window.packetReceiver.running = True
                self.main_window.start_receiving()
                return False
        else:
            print("loginReq에서 else문")
            socket = self.socket
        
        print("loginRequest의 socket")
        print(self.socket)
        socket = self.socket
        # socket = self.socket
        # self.main_window.packetReceiver.running = True
        # self.main_window.start_receiving()
        
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
            self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.home)
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
    
    def disconnect(self):
        self.main_window.ui.btn_login.show()
        self.main_window.ui.btn_home.hide()
        self.main_window.ui.btn_admin.hide()
        self.main_window.ui.btn_notice.hide()
        self.main_window.ui.btn_grafana.hide()
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.loginpage)
        self.main_window.packetReceiver.running = False
        self.main_window.receive_thread.join()
        print("스레드종료")
        if self.main_window.socket:
            self.main_window.socket.close()
            self.main_window.socket = None
            print("소켓 종료됨")
        else:
            print("소켓이 이미 닫혔거나 유효하지 않습니다.")
        
        # self.main_window.receive_thread.join()
        # print("스레드종료")

        
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
                        "login_id": self.signupId, 
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
        print("sendMsg 진입함")
        msgText = self.main_window.home_lineedit_chatlist_send.text()
        print(msgText)
        userId = self.main_window.userId
        groupname = getClickedRow("string", self.main_window.home_listview_chatgroup, self.main_window.groupListModel)
        
        try:
            msg = {"type": TYPE_MESSAGE,
                   "login_id": userId,
                   "groupname": groupname,
                   "text": msgText}
            
            packet = jsonParser(msg)
        
            if socket and msg:
                socket.sendall(packet)
            
            print(packet)
            self.main_window.updateMsgDisplay(msgText, "sent")
            
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def reqUserList(self, socket):
        try:
            msg = {"type": TYPE_USERLIST}
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
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def sendEditedMember(self, socket):
        groupname = getClickedRow("string", self.main_window.home_listview_chatgroup, self.main_window.groupListModel)
        inMember = self.main_window.memberAddDialog.in_member
        outMember = self.main_window.memberAddDialog.out_member
        try:
            msg = {"type": TYPE_EDIT_GROUP_MEMBER,
                   "groupname": groupname,
                   "in_member": inMember,
                   "out_member": outMember}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            print(packet)
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
        
    def reqGroupMemberList(self, socket):
        groupname = getClickedRow("string", self.main_window.home_listview_chatgroup, self.main_window.groupListModel)
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
        
    def reqAcceptList(self, socket):
        try:
            msg = {"type": 8}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def acceptReq(self, socket):
        selected_indexes = self.main_window.admin_listView_status.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = self.main_window.adminReqListModel.itemFromIndex(index)
            json_data = item.data(Qt.UserRole)
        
        signup_type = 'login_id'
        group_type = 'group_name'
        
        if signup_type in json_data:
            login_id = json_data["login_id"]
            dept = self.main_window.admin_combo_dept.currentText()
            pos = self.main_window.admin_combo_position.currentText()
            role = self.main_window.admin_combo_role.currentText()
            tps = self.main_window.admin_combo_tps.currentText()
            
            if dept == "1팀":
                dept = 1
            elif dept == "2팀":
                dept = 2
            elif dept == "3팀":
                dept = 3
            else:
                dept = 4
            
            if pos == "회장":
                pos = 1
            elif pos == "사장":
                pos = 2
            elif pos == "차장":
                pos = 3
            elif pos == "과장":
                pos = 4
            elif pos == "대리":
                pos = 5
            elif pos == "사원":
                pos = 6
            
            try:
                msg = {
                        "type": TYPE_ACCEPT_SIGNUP,
                        "is_ok": 1,
                        "login_id": login_id,
                        "dept": dept, 
                        "pos": pos, 
                        "role": int(role),
                        "max_tps": int(tps)
                    }
                packet = jsonParser(msg)
                print(msg)
                if socket and msg:
                    socket.sendall(packet)
                print(packet)
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        
        if group_type in json_data:
            groupname = json_data["group_name"]
            try:
                msg = {"type": TYPE_ACCEPT_GROUP,
                       "is_ok": 1,
                       "groupname": groupname}
                packet = jsonParser(msg)
                print(msg)
                if socket and msg:
                    socket.sendall(packet)
                print(packet)
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
    
    def rejectReq(self, socket):
        selected_indexes = self.main_window.admin_listView_status.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = self.main_window.adminReqListModel.itemFromIndex(index)
            json_data = item.data(Qt.UserRole)
        
        if firstKey(json_data) == "login_id":
            login_id = json_data["login_id"]
            try:
                msg = {
                        "type": TYPE_ACCEPT_SIGNUP,
                        "is_ok": 0,
                        "login_id": login_id
                    }
                packet = jsonParser(msg)
                if socket and msg:
                    socket.sendall(packet)
                print(packet)
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            groupname = json_data["group_name"]
            try:
                msg = {
                        "type": TYPE_ACCEPT_GROUP,
                        "is_ok": 0,
                        "groupname": groupname
                    }
                packet = jsonParser(msg)
                if socket and msg:
                    socket.sendall(packet)
                print(packet)
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
    
    def editUserReq(self, socket):
        print("edit user req 진입")
        self.userEditId = self.main_window.useredit_edit_id.text()
        self.userEditName = self.main_window.useredit_edit_name.text()
        self.userEditPhone = self.main_window.useredit_edit_phone.text()
        self.userEditEmail = self.main_window.useredit_edit_email.text()
        dept = self.main_window.useredit_combo_dept.currentText()
        pos = self.main_window.useredit_combo_position.currentText()
        role = int(self.main_window.useredit_combo_role.currentText())
        tps = int(self.main_window.useredit_combo_tps.currentText())

        print("if 문 진입")

        if role == "역할을 선택하세요.":
            role = ""

        if tps == "tps을 선택하세요.":
            tps = ""

        if dept == "부서를 선택하세요.":
            dept = ""
        elif dept == "1팀":
            dept = 1
        elif dept == "2팀":
            dept = 2
        elif dept == "3팀":
            dept = 3
        else:
            dept = 4
            
        if pos == "직급을 선택하세요.":
            pos = ""
        elif pos == "회장":
            pos = 1
        elif pos == "사장":
            pos = 2
        elif pos == "차장":
            pos = 3
        elif pos == "과장":
            pos = 4
        elif pos == "대리":
            pos = 5
        elif pos == "사원":
            pos = 6

        print("if문 완료")
        try:
            print("try문 진입")
            msg = {
                "type": TPPE_EDIT_USERINFO,
                "login_id": self.userEditId, 
                "name": self.userEditName,
                "phone": self.userEditPhone,
                "email": self.userEditEmail,
                "dept": dept,
                "pos": pos,
                "role": role,
                "max_tps": tps
            }
            packet = jsonParser(msg)
            
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
                print(f"An error occurred: {e}")
                return False

    
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

def firstKey(dictionary):
    if dictionary:
        return next(iter(dictionary))
    return None