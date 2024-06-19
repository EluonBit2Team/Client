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
from modules.send_packet import *
from modules.receive_socket import *
from modules import *
from modules.ui_noticedlg_function import *
from modules.ui_fooddlg_function import *
from modules.ui_groupadddlg_function import *
from modules.calldlg_function import *
from modules.mail_function import *
from modules.ui_adminpage_function import *
from widgets import *

SERVER_ADDR = "192.168.0.253"
# SERVER_ADDR = "127.0.0.1"
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
        initialize_widgets(self)
        initialize_variable(self)
        
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
        
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_admin.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)
        widgets.btn_notice.clicked.connect(self.buttonClick)
        widgets.home_btn_chatlist_send.clicked.connect(self.handleSendButtonClick) # 전송 버튼
        widgets.admin_btn_food.clicked.connect(self.show_food_dialog) # 오늘의 식단 버튼
        widgets.login_btn_call.clicked.connect(self.show_call_dialog) # 로그인 페이지의 전화 버튼
        widgets.login_btn_mail.clicked.connect(self.send_mail_btn) # 로그인 페이지의 메일 버튼

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

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        delegate = CustomDelegate(self.home_listview_chatlist)
        self.home_listview_chatlist.setItemDelegate(delegate)
        
        self.chatListModel = QStandardItemModel(self.home_listview_chatlist)
        self.home_listview_chatlist.setModel(self.chatListModel)
        
        self.groupListModel = QStandardItemModel(self.home_listview_chatgroup)
        self.home_listview_chatgroup.setModel(self.groupListModel)
        
        self.userListModel = QStandardItemModel(self.home_listview_status)
        self.home_listview_status.setModel(self.userListModel)
        
        self.userId = None
        self.socket = None
        self.packetSender = SendPacket(self)
        self.packetReceiver = ReceivePacket(self)
        self.groupDialog = GroupAddDialog(self)
        self.adminpage2 = MailFunctionWindow(self)
        
        #connect socket
        try:    
            self.packetSender.connectSocket(SERVER_ADDR, SERVER_PORT)
        except socket.error as e:
            print(f"Socket connection error: {e}")
            connectionErrorEvent()
        
        self.start_receiving()
        
        # self.packetSender.reqUserList(self.socket)
        # self.packetSender.reqGroupList(self.socket)

    # 약관체크버튼
    def toggleButton(self, state):
        if state == 2:
            self.signup_btn_submit.setEnabled(True)
        else:
            self.signup_btn_submit.setEnabled(False)
    
    # 알람 다이얼로그 함수
    def show_notice_dialog(self):
        dialog = CustomDialog(self)
        dialog.exec()

    # 오늘의 식단 보기 다이얼로그 함수
    def show_food_dialog(self):
        dialog = CustomDialog_food(self)
        dialog.exec()

    # 전화 다이얼로그 함수
    def show_call_dialog(self):
        dialog = CustomDialog_call(self)
        dialog.exec()

    # 메일 실행 함수
    def send_mail_btn(self):
        mailsend = MailFunctionWindow(self)
        mailsend.send_mail()
        
    def openDialog(self, dialogName):
        if dialogName == "GroupAddDialog":
            dialog = GroupAddDialog(self)
        elif dialogName == "CustomDialog_food":
            dialog = CustomDialog_food(self)
        dialog.exec()
    
    def handleSendButtonClick(self):
        # 클릭 시 아이콘 변경
        self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334 - 복사본.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))
        QTimer.singleShot(50, self.restoreSendButtonIcon)
    
    def restoreSendButtonIcon(self):
        # 원래 아이콘으로 복원
        self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))

    # 오늘의 식단 보기 함수
    def todaylunch(self):
        self.show_notice_dialog()
        
    # SET HOME PAGE AND SELECT MENU
    # ///////////////////////////////////////////////////////////////

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
    
    def updateMsgDisplay(self, message, messageType):
        item=QStandardItem(message)
        item.setData(messageType, Qt.ItemDataRole.UserRole + 1)
        self.chatListModel.appendRow(item)
        self.home_listview_chatlist.scrollToBottom()
    
    def updateDisplay(self, list, model):
        print("updateGroupDisplay 진입함")
        print(list)
        if model == "grouplist":
            for i in list:
                item=QStandardItem(i)
                self.groupListModel.appendRow(item)
        elif model == "userlist":
            # names = []
            # positions = []
            # departments = []
            # for item in list:
            #     names.append(item['name'])
            #     positions.append(item['position'])
            #     departments.append(item['dept_name'])
            
            for item in list:
                makeRow = item['dept_name'] + ' ' + item['position'] + ' ' + item['name']
                userRow = QStandardItem(makeRow)
                self.userListModel.appendRow(userRow)
            

    def loginRequest(self):
        self.packetSender.loginRequest(self.socket)
    
    def signUpRequest(self):
        self.packetSender.signUpRequest(self.socket)
            
    def sendMsg(self):
        self.packetSender.sendMsg(self.socket)
        self.home_lineedit_chatlist_send.clear()
        
    def receiveData(self):
        self.packetReceiver.receiveData(self.socket)
    

    def start_receiving(self):
        self.running = True
        receive_thread = threading.Thread(target=self.receiveData)
        receive_thread.daemon = True
        receive_thread.start()
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
