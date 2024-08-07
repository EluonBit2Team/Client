import json
import struct
import socket
from datetime import datetime, timedelta
from PySide6.QtWidgets import QMessageBox
from modules.util import *
from main import *
import threading
import time
request_thread = None
stop_thread_flag = False

class SendPacket:
    
    def __init__(self, main_window):
        self.main_window = main_window
        self.lock = threading.Lock()

    def connectSocket(self, addr, port):
        print("connectSocket진입")
        self.sock = self.main_window.socket
        try:
            if self.sock == None:
                print(f"Connecting to {addr}:{port}")

                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(5)

                self.sock.connect((addr, port))
                print(self.sock)
                # self.sock.setblocking(False)

                self.main_window.socket = self.sock
                return True
            else:
                print("socket else")
                self.sock.close()
                self.sock = None
                print(f"Connecting to {addr}:{port}")

                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(5)

                self.sock.connect((addr, port))
                
                self.main_window.socket = self.sock
                print(self.sock)
                # self.sock.setblocking(False)
                return True

        except Exception as e:
            self.main_window.isConnect = False
            self.main_window.login_btn_reconnect.show()
            print(f"An error occurred: {e}")
            return False
    
    def reconnect(self, sock):
        print("reconnect 진입")
        self.sock = sock
        self.sock = None
        self.connectSocket(SERVER_ADDR, SERVER_PORT)
        self.main_window.start_receiving()
        self.main_window.start_ping_thread()

    def sendPingData(self, sock):
        self.main_window.isFailed = True
        while self.main_window.isFailed:
            try:
                with self.lock:
                    if self.main_window.isConnect:
                        break
                    msg = {"type": 0}
                    packet = jsonParser(msg)
                    
                    if sock and msg:
                        sock.sendall(packet)
                    time.sleep(2)

            except socket.error as e:
                with self.lock:
                    self.main_window.setLoginPage()
                    self.main_window.isConnect = False
                    self.main_window.isFailed = False
                    print(f"Socket error occurred: {e}")
                    print("호스트와 연결이 끊어졌습니다.")
                    # QMessageBox.warning(self.main_window, 'Warning', '서버와의 연결이 끊어졌습니다.')
                    # self.connectSocket(SERVER_ADDR, SERVER_PORT)
                return False
        self.main_window.login_btn_reconnect.hide()
        print("연결됨")
        
    def loginRequest(self, sock):
        if sock == None:
            if not self.connectSocket(SERVER_ADDR, SERVER_PORT):
                print("Socket connection failed.")
                return False
            sock = self.main_window.sock
            self.main_window.packetReceiver.running = True
            self.main_window.start_receiving()
        else:
            sock = self.sock
            
        print(self.sock)
        sock = self.sock
        self.loginId = self.main_window.login_input_id.text()
        loginPw = self.main_window.login_input_pw.text()
        
        try:
            
            msg = {
                "type": TYPE_LOGIN,
                "login_id": self.loginId,
                "pw": loginPw
            }
            packet = jsonParser(msg)
            
            if sock and msg:
                sock.sendall(packet)
            
            print("login 패킷")
            print(packet)

            return True
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            self.connectSocket(SERVER_ADDR, SERVER_PORT)
            return False
    
    def qrLoginRequest(self, socket, msg):
        print(msg)
        try:
            packet = jsonParser(msg)

            if socket and msg:
                socket.sendall(packet)
            
            return True
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
    
    def disconnect(self):
        self.isLogin = True
        self.main_window.ui.btn_login.show()
        self.main_window.ui.btn_home.hide()
        self.main_window.ui.btn_admin.hide()
        self.main_window.ui.btn_notice.hide()
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.loginpage)
        self.main_window.packetReceiver.running = False
        print("스레드종료")
        if self.main_window.socket:
            self.main_window.socket.close()
            self.main_window.socket = None
            self.main_window.login_btn_reconnect.show()
            print("소켓 종료됨")
        else:
            print("소켓이 이미 닫혔거나 유효하지 않습니다.")
            
        if self.main_window.socket == None:
            if not self.connectSocket(SERVER_ADDR, SERVER_PORT):
                print("Socket connection failed.")
                return False
            self.main_window.packetReceiver.running = True
            self.main_window.start_receiving()
            self.main_window.start_ping_thread()
    
    def signUpRequest(self, socket):
        self.signupId = self.main_window.signup_input_id.text()
        self.signupPw = self.main_window.signup_input_pw.text()
        self.signupName = self.main_window.signup_input_name.text()
        self.signupPhone = self.main_window.signup_input_phone.text()
        self.signupEmail = self.main_window.signup_input_email.text()
        
        try:
            msg = {"type": TYPE_SIGNUP_REQ,
                        "login_id": self.signupId, 
                        "pw": self.signupPw,
                        "name": self.signupName,
                        "phone": self.signupPhone,
                        "email": self.signupEmail}
            packet = jsonParser(msg)
            
            print(packet)
        
            if socket and msg:
                socket.sendall(packet)
            return True
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
    
    def sendMsg(self, socket):
        if not self.main_window.sendTarget:
            return
        
        print("현재 sendTarget = " + self.main_window.sendTarget)
        if self.main_window.sendTarget == "group":
            print("그룹메세지")
            msgText = self.main_window.home_lineedit_chatlist_send.text()
            if not msgText:
                msgText = " "
            if len(msgText) > 400:
                self.main_window.alertMsgBox("400자 이하로 작성해주세요")
                return
            userId = self.main_window.userId
            groupname = getClickedRow("string", self.main_window.home_listview_chatgroup, self.main_window.groupListModel)
            print("userId = " + userId)
            print("groupname = " + groupname)
            print("msgText = " + msgText)
            
            try:
                msg = {"type": TYPE_MESSAGE,
                    "login_id": userId,
                    "groupname": groupname,
                    "text": msgText}
                
                print("msg")
                print(msg)
                
                packet = jsonParser(msg)
            
                if socket and msg:
                    socket.sendall(packet)
                
                print(packet)
                self.main_window.home_lineedit_chatlist_send.clear()
                return True
            except Exception as e:
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                return False
        
        elif self.main_window.sendTarget == "user":
            print("개인메세지")
            sendTo = self.main_window.nowClickedRow['login_id']
            msgText = self.main_window.home_lineedit_chatlist_send.text()
            if not msgText:
                msgText = " "
            print("보낸사람: " + self.main_window.userId)
            print("받는사람: " + sendTo)
            try:
                msg = {"type": TYPE_DM_SEND,
                    "sender_login_id" : self.main_window.userId,
                    "recver_login_id" : sendTo,
                    "text" : msgText
                    }
                packet = jsonParser(msg)
            
                if socket and msg:
                    socket.sendall(packet)
                    
                self.main_window.home_lineedit_chatlist_send.clear()
                return True
            except Exception as e:
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                return False
    
    def reqUserList(self, socket):
        try:
            msg = {"type": TYPE_USERLIST}
            packet = jsonParser(msg)
        
            if socket and msg:
                socket.sendall(packet)
                
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            self.connectSocket(SERVER_ADDR, SERVER_PORT)
            return False
    
    def reqOnlineList(self, socket):
        try:
            msg = {"type": TYPE_CURRENT_USERLIST}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            self.connectSocket(SERVER_ADDR, SERVER_PORT)
            return False
    
    def reqGroupList(self, socket):
        try:
            msg = {"type": TYPE_GROUPLIST}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            self.connectSocket(SERVER_ADDR, SERVER_PORT)
            return False
    
    def reqGroupChat(self, socket):
        now = datetime.now()
        utc_time = now - timedelta(hours=9)
        str_now = utc_time.isoformat().replace('T', ' ')
        start_time = datetime.now() - timedelta(days=3) - timedelta(hours=9)
        str_start_time = start_time.isoformat().replace('T', ' ')
        groupname = self.main_window.nowClickedRow['groupname']
        print("그룹네임 : " + groupname)
        try:
            msg = {
                "type": TYPE_GROUP_CHAT_REQ,
                "groupname": groupname,
                "start_time": str_start_time,
                "end_time": str_now
            }
            
            packet = jsonParser(msg)
            print("그룹 채팅기록 요청")
            print(packet)
            
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
    
    def sendEditedMember(self, socket):
        groupname = getClickedRow("string", self.main_window.home_listview_chatgroup, self.main_window.groupListModel)
        inMember = self.main_window.memberAddDialog.in_member
        outMember = self.main_window.memberAddDialog.out_member
        
        inMember, outMember = removeDuplicate(inMember, outMember)
        
        print("추가할 멤버")
        print(inMember)
        
        try:
            msg = {"type": TYPE_EDIT_GROUP_MEMBER,
                   "groupname": groupname,
                   "in_member": inMember,
                   "out_member": outMember}
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            
            if not inMember and not outMember:
                self.main_window.alertMsgBox("추가하거나 제외한 사람이 없습니다")
                return
            
            inMember.clear()
            outMember.clear()
            
            print(packet)
        except Exception as e:
            self.main_window.isConnect = False
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
            self.main_window.isConnect = False
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
            self.main_window.isConnect = False
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

            dept = sortUserInfo(dept, "dept")
            pos = sortUserInfo(pos, "pos")
            role = sortUserInfo(role, "role")
            tps = sortUserInfo(tps, "tps")
            
            print(dept)
            print(pos)
            print(role)
            print(tps)
            
            try:
                if 999 in [dept, pos, role, tps]:
                    self.main_window.alertMsgBox("회원정보에 누락된 내용이 없는지 확인해주세요")
                else:
                    msg = {
                            "type": TYPE_ACCEPT_SIGNUP,
                            "is_ok": 1,
                            "login_id": login_id,
                            "dept": dept,
                            "pos": pos,
                            "role": role,
                            "max_tps": tps
                        }
                    packet = jsonParser(msg)
                    print(msg)
                    if socket and msg:
                        socket.sendall(packet)
                    print(packet)
                    
            except Exception as e:
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                self.connectSocket(SERVER_ADDR, SERVER_PORT)
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
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                self.connectSocket(SERVER_ADDR, SERVER_PORT)
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
                self.main_window.isConnect = False
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
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                return False
    
    def editUserReq(self, socket):
        self.userEditId = self.main_window.useredit_edit_id.text()
        self.userEditName = self.main_window.useredit_edit_name.text()
        self.userEditPhone = self.main_window.useredit_edit_phone.text()
        self.userEditEmail = self.main_window.useredit_edit_email.text()
        dept = self.main_window.useredit_combo_dept.currentText()
        pos = self.main_window.useredit_combo_position.currentText()
        role = self.main_window.useredit_combo_role.currentText()
        tps = self.main_window.useredit_combo_tps.currentText()

        try:
            msg = {
                "type": TYPE_EDIT_USERINFO,
                "login_id": self.userEditId, 
                "name": self.userEditName,
                "phone": self.userEditPhone,
                "email": self.userEditEmail,
                "dept": sortUserInfo(dept, "dept"),
                "pos": sortUserInfo(pos, "pos"),
                "role": sortUserInfo(role, "role"),
                "max_tps": sortUserInfo(tps, "tps")
            }
            packet = jsonParser(msg)
            print("회원수정 packet")
            print(packet)
            
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
        
    # 그룹 삭제 요청
    def groupdeleteReq(self, socket):
        groupname = self.main_window.nowClickedRow['groupname']
        try:
            msg = {
                "type": TYPE_GROUPDELETE_REQ,
                "groupname": groupname
            }
            
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
    
    # 서버 로그 요청
    def serverlogReq(self, socket):
        # QCalendarWidget에서 선택된 날짜 가져오기
        selected_date = self.main_window.log_calendarwidget_cal.selectedDate()

        # updateStartTime 함수를 호출하여 start_time과 end_time을 업데이트
        start_time, end_time = updateStartTime(selected_date)

        try:
            msg = {
                "type": TYPE_LOG_REQ,
                "start_time": start_time,
                "end_time": end_time
            }
            packet = jsonParser(msg)
            print("서버 로그 요청 packet")
            print(packet)
            
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
    
    def reqDm(self, socket):
        now = datetime.now()
        utc_time = now - timedelta(hours=9)
        str_now = utc_time.isoformat().replace('T', ' ')
        start_time = datetime.now() - timedelta(days=3) - timedelta(hours=9)
        str_start_time = start_time.isoformat().replace('T', ' ')
        try:
            msg = {
                "type": TYPE_DM_LOG,
                "recver_login_id": self.main_window.nowClickedRow['login_id'],
                "start_time": str_start_time,
                "end_time": str_now
            }
            packet = jsonParser(msg)
            print("개인채팅로그요청")
            print(packet)
            
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
        
    
    def searchChatLog(self, socket):
        self.main_window.listMode = "log"
        start_time = self.main_window.setLogTime.start_time 
        end_time = self.main_window.setLogTime.end_time + ' 23:59:59'
        start_time_to_datetime = datetime.strptime(start_time, "%Y-%m-%d") - timedelta(hours=9)
        end_time_to_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") - timedelta(hours=9)
        str_start_time = start_time_to_datetime.isoformat().replace('T', ' ')
        str_end_time = end_time_to_datetime.isoformat().replace('T', ' ')
        print(str_start_time + "부터 "+ str_end_time + "까지의 데이터")
        print("nowClickedRow")
        print(self.main_window.nowClickedRow)
        first_key = next(iter(self.main_window.nowClickedRow))
        if first_key == 'groupname':
            try:
                msg = {
                    "type": TYPE_GROUP_CHAT_REQ,
                    "groupname": self.main_window.nowClickedRow['groupname'],
                    "start_time": str_start_time,
                    "end_time": str_end_time
                }
                packet = jsonParser(msg)
                print("그룹채팅로그요청")
                print(packet)
                
                if socket and msg:
                    socket.sendall(packet)

            except Exception as e:
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                return False
        
        elif first_key == 'login_id':
            try:
                msg = {
                    "type": TYPE_DM_LOG,
                    "recver_login_id": self.main_window.nowClickedRow['login_id'],
                    "start_time": str_start_time,
                    "end_time": str_end_time
                }
                packet = jsonParser(msg)
                print("개인채팅로그요청")
                print(packet)
                
                if socket and msg:
                    socket.sendall(packet)

            except Exception as e:
                self.main_window.isConnect = False
                print(f"An error occurred: {e}")
                return False
        
        self.main_window.home_btn_return_chat.show()
        
    # 서버 실시간 상태 요청
    def serverrealtimeReq(self, socket, interval):
        print("서버로그 스레드 시작")
        self.stop_thread_flag = True
        while self.stop_thread_flag:
            try:
                msg = {
                    "type": TYPE_REALTIME_REQ,
                }
                packet = jsonParser(msg)
                print("서버 실시간 상태 요청 packet")
                print(packet)
                
                if socket and msg:
                    socket.sendall(packet)

            except Exception as e:
                print(f"An error occurred: {e}")
                self.main_window.isConnect = False
                self.stop_thread_flag = False
                return False
            
            time.sleep(interval)
    
    def leaveGroup(self, socket):
        groupname = self.main_window.nowClickedRow['groupname']
        try:
            msg = {
                "type": TYPE_LEAVE_GROUP,
                "groupname": groupname
            }
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False
        
    # 유저 로그 요청
    def userlogReq(self, socket):
        # QCalendarWidget에서 선택된 날짜 가져오기
        selected_date = self.main_window.userlog_calendarwidget_cal.selectedDate()

        # updateStartTime 함수를 호출하여 start_time과 end_time을 업데이트
        start_time, end_time = updateStartTime(selected_date)

        try:
            msg = {
                "type": TYPE_USERLOG_REQ,
                "start_time": start_time,
                "end_time": end_time
            }
            packet = jsonParser(msg)
            print("서버 로그 요청 packet")
            print(packet)
            
            if socket and msg:
                socket.sendall(packet)

        except Exception as e:
            self.main_window.isConnect = False
            print(f"An error occurred: {e}")
            return False

    def testDataSender(self, socket):
        print("type: 14 보냄")
        try:
            msg = {
                "type": 14,
                "groupname": "groupname1" 
            }
            packet = jsonParser(msg)
            if socket and msg:
                socket.sendall(packet)
            print(msg)
        except Exception as e:
            self.main_window.isConnect = False
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