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
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules.util import *
from modules import *
from widgets import *
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

        self.admin_btn_accept = self.findChild(QPushButton, "admin_btn_accept")
        self.admin_btn_reject = self.findChild(QPushButton, "admin_btn_reject")


        self.btn_home = self.findChild(QPushButton, "btn_home")
        self.btn_admin = self.findChild(QPushButton, "btn_admin")
        self.btn_save = self.findChild(QPushButton, "btn_save")

        #hide menu
        # self.btn_home.hide()
        # self.btn_admin.hide()
        # self.btn_save.hide()

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
        
        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def loginRequest(self):
        self.host = self.login_input_id.text()
        self.port = self.login_input_pw.text()
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, int(self.port)))
            self.socket.setblocking(False)
            #self.start_receiving()
            self.btn_home.show()
            self.btn_admin.show()
            self.btn_save.show()
            self.connectionSuccessEvent()
        except Exception:
            self.connectionErrorEvent()
    
    def connectionErrorEvent(self):
        QMessageBox.warning(self, "Error", "연결 실패")

    def connectionSuccessEvent(self):
        QMessageBox.information(self, "Success", "연결 성공")

    def signUpRequest(self):
        self.signupId = self.signup_input_id.text()
        self.signupPw = self.signup_input_pw.text()
        self.signupName = self.signup_input_name.text()
        self.signupPhone = self.signup_input_phone.text()
        self.signupEmail = self.signup_input_email.text()
        self.signupDept = self.signup_combo_dept.currentText()
        self.signupPosition = self.signup_combo_position.currentText()

        QMessageBox.information(self, "SignUp", "id: " + self.signupId + '\n'
                                                "pw: " + self.signupPw + '\n'
                                                "name: " + self.signupName + '\n'
                                                "Phone: " + self.signupPhone + '\n'
                                                "Email: " + self.signupEmail + '\n'
                                                "Dept: " + self.signupDept + '\n'
                                                "Position: " + self.signupPosition + '\n')


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
