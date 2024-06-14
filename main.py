# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import socket
import select
import threading
import json
import struct
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules.util import *
from modules.ui_initialization import *
from modules import *
from modules.ui_notice_dlg import *
from widgets import *

SERVER_ADDR = "192.168.0.253"
SERVER_PORT = 3335

# SERVER_ADDR = "127.0.0.1"
# SERVER_PORT = 40112


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%



# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        #widgets initialize
        initialize_widgets(self)

        #hide menu
        # self.btn_home.hide()
        # self.btn_admin.hide()
        # self.btn_notice.hide()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "TalkTalk"
        description = "TalkTalk :: 모두 함께 소통하는 회사"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_admin.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)
        widgets.btn_notice.clicked.connect(self.buttonClick)
        widgets.home_btn_chatlist_send.clicked.connect(self.handleSendButtonClick) # 전송 버튼
        


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # LOGIN PAGE
        widgets.login_btn_signup.clicked.connect(self.buttonClick) #회원가입 버튼 이벤트
        widgets.signup_btn_back.clicked.connect(self.buttonClick)
        


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        try:
            self.connectSocket(SERVER_ADDR, SERVER_PORT)
        except socket.error as e:
            print(f"Socket connection error: {e}")
            connectionErrorEvent()
            
        delegate = CustomDelegate(self.home_listview_chatlist)
        self.home_listview_chatlist.setItemDelegate(delegate)
        
        self.chatList = []
        self.chatListModel = QStandardItemModel(self.home_listview_chatlist)
        self.home_listview_chatlist.setModel(self.chatListModel)
    


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def toggleButton(self, state):
        if state == 2:
            self.signup_btn_submit.setEnabled(True)
        else:
            self.signup_btn_submit.setEnabled(False)
        
    def show_notice_dialog(self):
        dialog = CustomDialog(self)
        dialog.exec()

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        UIFunctions.resetStyle(self, btnName)

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_admin":
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW LOGIN PAGE
        if (btnName == "btn_login") or (btnName == "signup_btn_back"):
            widgets.stackedWidget.setCurrentWidget(widgets.loginpage) # SET PAGE
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW SIGNUP PAGE
        if btnName == "login_btn_signup":
            widgets.stackedWidget.setCurrentWidget(widgets.signuppage) # SET PAGE
           # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "btn_notice":
            # 버튼 클릭 시 다이얼로그 호출
            self.show_notice_dialog()

        
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    
    def connectSocket(self, addr, port):
        try:
            print(f"Connecting to {addr}:{port}")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((addr, port))
            self.socket.setblocking(False)
            connectionSuccessEvent()
        except socket.error as e:
            print(f"Socket connection error: {e}")
            connectionErrorEvent()

    def loginRequest(self):
        self.loginId = self.login_input_id.text()
        self.loginPw = self.login_input_pw.text()
        try:
            msg = {"type": 2,
                        "id": self.loginId, 
                        "pw": self.loginPw}
            json_msg = json.dumps(msg, ensure_ascii=False)
            msg_length = len(json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)
        
            if self.socket and msg:
                self.socket.sendall(header + json_msg.encode('utf-8'))
            print(total_length)
            print(json_msg)
            
            QMessageBox.information(self, "보낸정보", "id: " + self.loginId + '\n'
                                                    "pw: " + self.loginPw + '\n')

            self.start_receiving()
            
            self.btn_home.show()
            self.btn_admin.show()
            self.btn_notice.show()
            self.connectionSuccessEvent()
        except Exception:
            connectionErrorEvent()
    
    def signUpRequest(self):
        self.signupId = self.signup_input_id.text()
        self.signupPw = self.signup_input_pw.text()
        self.signupName = self.signup_input_name.text()
        self.signupPhone = self.signup_input_phone.text()
        self.signupEmail = self.signup_input_email.text()
        self.signupDept = self.signup_combo_dept.currentText()
        self.signupPosition = self.signup_combo_position.currentText()
        
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
                        "id": "아이디", 
                        "pw": "비번",
                        "name": "이름",
                        "phone": "폰번",
                        "email": "이메일",
                        "dept": "부서",
                        "pos": "직급"}
            json_msg = json.dumps(msg, ensure_ascii=False)
            byte_json_msg = bytes(json_msg, 'utf-8')
            msg_length = len(byte_json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)
        
            if self.socket and msg:
                self.socket.sendall(header + json_msg.encode('utf-8'))
            print(total_length)
            print(json_msg)

            QMessageBox.information(self, "SignUp", "id: " + self.signupId + '\n'
                                                "pw: " + self.signupPw + '\n'
                                                "name: " + self.signupName + '\n'
                                                "Phone: " + self.signupPhone + '\n'
                                                "Email: " + self.signupEmail + '\n'
                                                "Dept: " + self.signupDept + '\n'
                                                "Position: " + self.signupPosition + '\n')
            connectionSuccessEvent()
        except Exception:
            connectionErrorEvent()

    def handleSendButtonClick(self):
        # 클릭 시 아이콘 변경
        self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334 - 복사본.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))
        # 메시지 전송 함수 호출
        self.sendMsg()
        
        # 원래 아이콘으로 복원
        self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))

    def sendMsg(self):
        QCoreApplication.processEvents()  # 프로세스 이벤트를 처리하여 UI 업데이트
        QThread.msleep(50) # 전송버튼 sleep

        # self.msgText = self.home_lineedit_chatlist_send.text()
        # self.loginId = "eluon"
        # self.groupName = "채팅방 1"
        # try:
        #     msg = {"type": 0,
        #            "id": self.loginId,
        #            "groupname": self.groupName,
        #            "text": self.msgText}
        
        #     json_msg = json.dumps(msg, ensure_ascii=False)
        #     msg_length = len(json_msg)
        #     total_length = msg_length + 4
        #     header = struct.pack('<I', total_length)
        
        #     if self.socket and msg:
        #         self.socket.sendall(header + json_msg.encode('utf-8'))
            
        #     print(total_length)
        #     print(json_msg)
        #     self.updateMsgDisplay(self.msgText, "sent")
            
        
        # except BlockingIOError:
        #     connectionErrorEvent()
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        #     self.running = False
    
    def receive_message(self):
        buffer = b""
        while self.running:
            try:
                if self.socket:
                    readable, _, _ = select.select([self.socket], [], [], 0.5)
                    if readable:
                        data = self.socket.recv(4096)
                        if data:
                            buffer += data
                            while len(buffer) >= 4:
                                msg_length = struct.unpack('<I', buffer[:4])[0]
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:4 + msg_length]
                                    buffer = buffer[4 + msg_length:]
                                    message = json.loads(json_msg.decode('utf-8')).get("text")
                                    self.updateMsgDisplay(message, "received")
                                
                                else:
                                    break
            except BlockingIOError:
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False
            

    def start_receiving(self):
        self.running = True
        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.daemon = True
        receive_thread.start()
    
    def updateMsgDisplay(self, message, messageType):
        item=QStandardItem(message)
        item.setData(messageType, Qt.ItemDataRole.UserRole + 1)
        self.chatListModel.appendRow(item)
        # self.chatList.append(message)
        # self.chatListModel.setStringList(self.chatList)
        self.home_listview_chatlist.scrollToBottom()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
