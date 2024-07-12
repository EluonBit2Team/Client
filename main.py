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
import time
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
from modules.ui_chatmemberadd_function import *
from modules.ui_calldlg_function import *
from modules.mail_function import *
from modules.ui_adminpage_function import *
from modules.ui_groupmemberlistdlg_function import *
from modules.qrcode import *
from modules.ui_grafana_function import *
from modules.ui_loadingsp import *
from modules.ui_setlogtimedlg_function import *
from widgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"


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

        # 로딩 GIF 보여주기
        # self.loadingGif = LoadingGif()
        # self.loadingGif.show()
        # self.loadingGif.startAnimation()

        # widgets initialize
        initialize_widgets(self)
        initialize_variable(self)
        

        # hide menu
        self.btn_home.hide()
        self.btn_admin.hide()
        self.btn_notice.hide()
        self.home_btn_return_chat.hide()
        self.login_btn_reconnect.hide()
        self.admin_label_new.hide()
        self.home_btn_search_chat.hide()
        self.home_btn_groupmemberlist.hide()
        self.home_btn_add_member.hide()

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
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_admin.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)

        # Main button
        widgets.home_btn_chatlist_send.clicked.connect(
            self.handleSendButtonClick)  # 전송 버튼

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # LOGIN PAGE
        widgets.login_btn_signup.clicked.connect(self.buttonClick)
        widgets.login_btn_qrlogin.clicked.connect(self.buttonClick)
        widgets.signup_btn_back.clicked.connect(self.buttonClick)
        widgets.qrlogin_btn_back.clicked.connect(self.buttonClick)
        widgets.admin_btn_useredit.clicked.connect(self.buttonClick)
        widgets.useredit_btn_back.clicked.connect(self.buttonClick)
        widgets.admin_btn_log.clicked.connect(self.buttonClick)
        widgets.admin_btn_server.clicked.connect(self.buttonClick)
        widgets.log_btn_back.clicked.connect(self.buttonClick)
        widgets.serverstate_btn_back.clicked.connect(self.buttonClick)
        widgets.userlog_btn_back.clicked.connect(self.buttonClick)
        widgets.admin_btn_conlog.clicked.connect(self.buttonClick)
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

        widgets.stackedWidget.setCurrentWidget(widgets.loginpage)

        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        delegate = CustomDelegate(self.home_listview_chatlist)
        self.home_listview_chatlist.setItemDelegate(delegate)

        self.chatListModel = QStandardItemModel(self.home_listview_chatlist)
        self.home_listview_chatlist.setModel(self.chatListModel)
        self.home_listview_chatlist.setUniformItemSizes(False)
        # self.chatListModel.rowsInserted.connect(self.scroll_to_bottom)

        self.groupListModel = QStandardItemModel(self.home_listview_chatgroup)
        self.home_listview_chatgroup.setModel(self.groupListModel)
        
        self.adminReqListModel = QStandardItemModel(self.admin_listView_status)
        self.admin_listView_status.setModel(self.adminReqListModel)

        self.logReqListModel = QStandardItemModel(self.log_treview_log)
        self.log_treview_log.setModel(self.logReqListModel)

        self.loguserReqListModel = QStandardItemModel(self.userlog_treview_log)
        self.userlog_treview_log.setModel(self.loguserReqListModel)

        self.realtimememListModel = QStandardItemModel(self.serverstate_listview_mem)
        self.serverstate_listview_mem.setModel(self.realtimememListModel)

        self.realtimeloginListModel = QStandardItemModel(self.serverstate_listview_numuser)
        self.serverstate_listview_numuser.setModel(self.realtimeloginListModel)

        self.realtimetpsListModel = QStandardItemModel(self.serverstate_listview_packet)
        self.serverstate_listview_packet.setModel(self.realtimetpsListModel)

        self.userListModel = QStandardItemModel(self.home_treeview_userlist)
        self.home_treeview_userlist.setModel(self.userListModel)
        self.userListModel.setHorizontalHeaderLabels(["이름", "아이디"])

        self.useredit_treeview_userlist.setModel(self.userListModel)

        self.clientSession = ClientSession(self)
        self.packetSender = SendPacket(self)
        self.packetReceiver = ReceivePacket(self)
        self.qrcode = Qrcode(self)
        self.groupDialog = GroupAddDialog(self)
        self.groupMember = GroupMemberListDialog(self)
        self.memberAddDialog = MemberAddDialog(self)
        self.setLogTime = SetLogTimeDlg(self)
        self.lock = threading.Lock()
        
        self.btn_logout.clicked.connect(self.packetSender.disconnect)
        
        
        #connect socket
        self.packetSender.connectSocket(SERVER_ADDR, SERVER_PORT)
        # self.packetSender.reconnect(self.socket)
        self.start_receiving()
        self.start_ping_thread()
                
        print("main의 socket")
        print(self.socket)
    
    # 약관체크버튼
    def toggleButton(self, state):
        if state == 2:
            self.signup_btn_submit.setEnabled(True)
        else:
            self.signup_btn_submit.setEnabled(False)

    # 다이얼로그 호출
    def openDialog(self, dialogName):
        try:
            # 채팅 그룹 추가 다이얼로그
            if dialogName == "GroupAddDialog":
                dialog = self.groupDialog
            # 대화 상대 추가 다이얼로그
            elif dialogName == "MemberAddDialog":
                self.packetSender.reqGroupMemberList(self.socket)
                dialog = self.memberAddDialog
            # 이메일 다이얼로그
            elif dialogName == "MailFunctionWindow":
                dialog = MailFunctionWindow(self)
            # 전화 다이얼로그
            elif dialogName == "CallDialog":
                dialog = CallDialog(self)
            # 음식 다이얼로그
            elif dialogName == "FoodDialog":
                dialog = FoodDialog(self)
            # 알람 다이얼로그
            elif dialogName == "NoticeDialog":
                dialog = NoticeDialog(self)
            # 그라파나 다이얼로그
            elif dialogName == "GrafanaDialog":
                dialog = GrafanaDialog(self)  
            # 채팅방 유저 다이얼로그
            elif dialogName == "GroupMemberListDialog":
                self.packetSender.reqGroupMemberList(self.socket)
                dialog = self.groupMember
            elif dialogName == "SetLogTimeDlg":
                dialog = self.setLogTime
            
            dialog.exec()
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def handleSendButtonClick(self):
        # 클릭 시 아이콘 변경
        self.home_btn_chatlist_send.setIcon(
            QIcon(':/images/images/images/free-icon-send-button-12439334 - 복사본.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))
        QTimer.singleShot(50, self.restoreSendButtonIcon)

    def restoreSendButtonIcon(self):
        # 원래 아이콘으로 복원
        self.home_btn_chatlist_send.setIcon(
            QIcon(':/images/images/images/free-icon-send-button-12439334.png'))
        self.home_btn_chatlist_send.setIconSize(QSize(41, 41))

    

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
            self.packetSender.reqUserList(self.socket)
            self.packetSender.reqGroupList(self.socket)

        # SHOW ADMIN PAGE
        if btnName == "btn_admin":
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.packetSender.reqAcceptList(self.socket)

        # SHOW LOGIN PAGE
        if btnName == "btn_login":
            widgets.stackedWidget.setCurrentWidget(widgets.loginpage) # SET PAGE
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "signup_btn_back":
            self.signup_input_id.clear()
            self.signup_input_pw.clear()
            self.signup_input_name.clear()
            self.signup_input_phone.clear()
            self.signup_input_email.clear()
            animateTransitionBack(self.ui, widgets.signuppage, widgets.loginpage, setPage)
        
        if btnName == "qrlogin_btn_back":
            widgets.stackedWidget.setCurrentWidget(widgets.loginpage)
            self.qrcode.stop_qrcode()
        
        # SHOW QRLOGIN PAGE
        if btnName == "login_btn_qrlogin":
            widgets.stackedWidget.setCurrentWidget(widgets.qrlogin)
            self.qrcode.wait_qrcode()
            
        # SHOW SIGNUP PAGE
        if btnName == "login_btn_signup":
            animateTransition(self.ui, widgets.loginpage, widgets.signuppage, setPage)
            # widgets.stackedWidget.setCurrentWidget(widgets.signuppage)  # SET PAGE
           # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW USEREDIT PAGE
        if btnName == "admin_btn_useredit":
            widgets.stackedWidget.setCurrentWidget(widgets.infoeditpage)
            #self.packetSender.reqUserList(self.socket)
        if btnName == "useredit_btn_back":
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)

        # SHOW LOG PAGE
        if btnName == "admin_btn_log":
            widgets.stackedWidget.setCurrentWidget(widgets.serverlogpage)
        if btnName == "log_btn_back":
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)

        # SHOW USER LOG PAGE
        if btnName == "admin_btn_conlog":
            widgets.stackedWidget.setCurrentWidget(widgets.userlogpage)
            self.admin_label_new.hide()
            if isinstance(widgets.log_calendarwidget_cal, QCalendarWidget):
                today_date = QDate.currentDate()
                widgets.log_calendarwidget_cal.setSelectedDate(today_date)
            
        if btnName == "userlog_btn_back":
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)

        # SHOW SERVER PAGE
        if btnName == "admin_btn_server":
            widgets.stackedWidget.setCurrentWidget(widgets.serverstatepage)
        if btnName == "serverstate_btn_back":
            self.packetSender.stop_thread_flag = False
            print("스레드 종료")
            widgets.stackedWidget.setCurrentWidget(widgets.adminpage)
            
        if btnName == "btn_exit":
            self.packetSender.testDataSender(self.socket)
            
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
        
    #데이터를 받는 receiveData 스레드 실행
    def start_receiving(self):
        self.packetReceiver.running = True
        self.receive_thread = threading.Thread(target=self.packetReceiver.receiveData, args=(self.socket, ))
        self.receive_thread.start()
        
    #서버와의 연결을 체크하는 핑 스레드 실행
    def start_ping_thread(self):
        self.ping_thread = threading.Thread(target=self.packetSender.sendPingData, args=(self.socket,))
        self.ping_thread.start()
        
    def statusthread(self):
        print("statusthread 시작")
        request_thread = threading.Thread(target=self.packetSender.serverrealtimeReq, args=(self.socket, 10))
        request_thread.daemon = True
        request_thread.start()
        self.request_thread = request_thread
        print("서버 실시간 상태 요청 스레드 시작됨")
        
    def setLoginPage(self):
        widgets.stackedWidget.setCurrentWidget(widgets.loginpage)
    
    # @Slot()
    # def scroll_to_bottom(self):
    #     self.home_listview_chatlist.scrollToBottom()
    
    @Slot(str)
    def setDisconnect(self, alterMsg):
        self.login_btn_reconnect.show()
        self.btn_home.hide()
        self.btn_admin.hide()
        self.btn_notice.hide()
        widgets.stackedWidget.setCurrentWidget(widgets.loginpage)
        QMessageBox.warning(self, '경고', alterMsg, QMessageBox.Ok)
    
    @Slot(QObject)
    def updatePage(self, page):
         widgets.stackedWidget.setCurrentWidget(page)
        
    
    @Slot()
    def setGUILoginSucess(self, userId):
        print(userId + '가 로그인함')
        self.login_input_id.clear()
        self.login_input_pw.clear()
        self.chatListModel.clear()
        self.btn_home.show()
        if self.userRole == 1:
            self.btn_admin.show()
        else:
            self.btn_admin.hide()
        # if self.userRole == 1:
        #     self.btn_notice.show()
        # else:
        #     self.btn_notice.hide()
        self.btn_login.hide()
        widgets.stackedWidget.setCurrentWidget(widgets.home)
    
    @Slot(str)
    def alertMsgBox(self, alterMsg):
        QMessageBox.warning(self, '경고', alterMsg, QMessageBox.Ok)

    @Slot(list, list)
    def updateIcon(self, showIcon, hideIcon):
        if showIcon:
            for icon in showIcon:
                icon.show()
        
        if hideIcon:
            for icon in hideIcon:
                icon.hide()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '경고', 
            "프로그램을 종료하시겠습니까?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
            QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.socket.close()
            event.accept()
            QApplication.quit()
        else:
            event.ignore()
    



    # RESIZE EVENTSc
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