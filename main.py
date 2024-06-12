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
import json
import struct
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules.util import *
from modules import *
from widgets import *

SERVER_ADDR = "192.168.0.253"
SERVER_PORT = 3335



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
        self.login_input_id = self.findChild(QLineEdit, "login_input_id")
        self.login_input_pw = self.findChild(QLineEdit, "login_input_pw")
        self.login_btn_login = self.findChild(QPushButton, "login_btn_login")
        self.signup_input_id = self.findChild(QLineEdit, "signup_input_id")
        self.signup_input_pw = self.findChild(QLineEdit, "signup_input_pw")
        self.signup_input_name = self.findChild(QLineEdit, "signup_input_name")
        self.signup_input_phone = self.findChild(QLineEdit, "signup_input_phone")
        self.signup_input_email = self.findChild(QLineEdit, "signup_input_email")
        self.signup_combo_dept = self.findChild(QComboBox, "signup_combo_dept")
        self.signup_combo_position = self.findChild(QComboBox, "signup_combo_position")
        self.signup_btn_submit = self.findChild(QPushButton, "signup_btn_submit")
        self.signup_btn_back = self.findChild(QPushButton, "signup_btn_back")
        self.signup_checkbox_agree = self.findChild(QCheckBox, "signup_checkbox_agree")




        self.btn_home = self.findChild(QPushButton, "btn_home")
        self.btn_widgets = self.findChild(QPushButton, "btn_widgets")
        self.btn_save = self.findChild(QPushButton, "btn_save")

        #hide menu
        self.btn_home.hide()
        self.btn_widgets.hide()
        self.btn_save.hide()

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
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

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
        
        self.connectSocket(SERVER_ADDR, SERVER_PORT)
    


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def toggleButton(self, state):
        if state == 2:
            self.signup_btn_submit.setEnabled(True)
        else:
            self.signup_btn_submit.setEnabled(False)
        


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
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW LOGIN PAGE
        if (btnName == "btn_login") or (btnName == "signup_btn_back"):
            widgets.stackedWidget.setCurrentWidget(widgets.loginpage) # SET PAGE
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW SIGNUP PAGE
        if btnName == "login_btn_signup":
            widgets.stackedWidget.setCurrentWidget(widgets.signuppage) # SET PAGE
           # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    
    def connectSocket(self, addr, port):
        try:
            print(addr)
            print(port)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((addr, port))
            self.socket.setblocking(False)
            print("Socket connected")
            connectionSuccessEvent()
        except Exception:
            connectionErrorEvent()

    def loginRequest(self):
        self.loginId = self.login_input_id.text()
        self.loginPw = self.login_input_pw.text()
        try:
            loginReq = {"type": 2,
                        "id": self.loginId, 
                        "pw": self.loginPw}
            json_msg = json.dumps(loginReq)
            msg_length = len(json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)
        
            if self.socket and loginReq:
                self.socket.sendall(header + json_msg.encode('utf-8'))
            print(total_length)
            print(json_msg)
            
            QMessageBox.information(self, "보낸정보", "id: " + self.loginId + '\n'
                                                    "pw: " + self.loginPw + '\n')

            #self.start_receiving()
            
            self.btn_home.show()
            self.btn_widgets.show()
            self.btn_save.show()
            connectionSuccessEvent()
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
            loginReq = {"type": 1,
                        "id": self.signupId, 
                        "pw": self.signupPw,
                        "name": self.signupName,
                        "phone": self.signupPhone,
                        "email": self.signupEmail,
                        "dept": self.signupDept,
                        "pos": self.signupPosition}
            json_msg = json.dumps(loginReq)
            msg_length = len(json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)
        
            if self.socket and loginReq:
                self.socket.sendall(header + json_msg.encode('utf-8'))
            
            print("dept: " + self.signupDept)
            print("pos: " + self.signupPosition)
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
            
    def sendMsg(self):
        # self.userId = self.loginId
        # self.groupName = self.group_name.text()
        # self.msgText = self.home_input_msg.text()
        self.loginId = "eluon"
        self.groupName = "채팅방 1"
        self.msgText = "안녕하세요 hi hi"
        try:
            msg = {"type": 0,
                   "id": self.loginId,
                   "groupname": self.groupName,
                   "text": self.msgText}
        
            json_msg = json.dumps(msg)
            msg_length = len(json_msg)
            total_length = msg_length + 4
            header = struct.pack('<I', total_length)
        
            if self.socket and msg:
                self.socket.sendall(header + json_msg.encode('utf-8'))
            
            print(total_length)
            print(json_msg)
            connectionSuccessEvent()
        
        except Exception:
            connectionErrorEvent()
        
        


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
