from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def initialize_widgets(mainWindow: QMainWindow):
    mainWindow.btn_notice = mainWindow.findChild(QLineEdit, "btn_notice")

    mainWindow.login_input_id = mainWindow.findChild(QLineEdit, "login_input_id")
    mainWindow.login_input_pw = mainWindow.findChild(QLineEdit, "login_input_pw")
    mainWindow.login_btn_login = mainWindow.findChild(QPushButton, "login_btn_login")
    mainWindow.login_btn_mail = mainWindow.findChild(QPushButton, "login_btn_mail")
    mainWindow.login_btn_call = mainWindow.findChild(QPushButton, "login_btn_call")
    mainWindow.login_btn_qrlogin = mainWindow.findChild(QPushButton, "login_btn_qrlogin")

    mainWindow.qrlogin_btn_back = mainWindow.findChild(QPushButton, "qrlogin_btn_back")
    mainWindow.qrlogin_label_waiting = mainWindow.findChild(QLabel, "qrlogin_label_waiting")

    mainWindow.signup_input_id = mainWindow.findChild(QLineEdit, "signup_input_id")
    mainWindow.signup_input_pw = mainWindow.findChild(QLineEdit, "signup_input_pw")
    mainWindow.signup_input_name = mainWindow.findChild(QLineEdit, "signup_input_name")
    mainWindow.signup_input_phone = mainWindow.findChild(QLineEdit, "signup_input_phone")
    mainWindow.signup_input_email = mainWindow.findChild(QLineEdit, "signup_input_email")
    mainWindow.signup_combo_dept = mainWindow.findChild(QComboBox, "signup_combo_dept")
    mainWindow.signup_combo_position = mainWindow.findChild(QComboBox, "signup_combo_position")
    mainWindow.signup_btn_submit = mainWindow.findChild(QPushButton, "signup_btn_submit")
    mainWindow.signup_btn_back = mainWindow.findChild(QPushButton, "signup_btn_back")
    mainWindow.signup_checkbox_agree = mainWindow.findChild(QCheckBox, "signup_checkbox_agree")
    
    mainWindow.home_lineedit_chatlist_send = mainWindow.findChild(QLineEdit, "home_lineedit_chatlist_send")
    mainWindow.home_btn_chatlist_send = mainWindow.findChild(QPushButton, "home_btn_chatlist_send")
    mainWindow.home_listview_chatlist = mainWindow.findChild(QListView, "home_listview_chatlist")
    mainWindow.home_listview_chatgroup = mainWindow.findChild(QListView, "home_listview_chatgroup")
    mainWindow.home_treeview_userlist = mainWindow.findChild(QTreeView, "home_treeview_userlist")
    mainWindow.home_btn_chatgroup = mainWindow.findChild(QPushButton, "home_btn_chatgroup")
    mainWindow.home_btn_add_member = mainWindow.findChild(QPushButton, "home_btn_add_member")
    mainWindow.home_btn_right = mainWindow.findChild(QPushButton, "home_btn_right")
    mainWindow.home_btn_left = mainWindow.findChild(QPushButton, "home_btn_left")
    mainWindow.home_btn_groupmemberlist = mainWindow.findChild(QPushButton, "home_btn_groupmemberlist")

    mainWindow.admin_btn_accept = mainWindow.findChild(QPushButton, "admin_btn_accept")
    mainWindow.admin_btn_reject = mainWindow.findChild(QPushButton, "admin_btn_reject")
    mainWindow.admin_btn_food = mainWindow.findChild(QPushButton, "admin_btn_food")
    mainWindow.admin_listView_status = mainWindow.findChild(QListView, "admin_listView_status")
    mainWindow.admin_combo_dept = mainWindow.findChild(QComboBox, "admin_combo_dept")
    mainWindow.admin_combo_position = mainWindow.findChild(QComboBox, "admin_combo_position")
    mainWindow.admin_combo_role = mainWindow.findChild(QComboBox, "admin_combo_role")
    mainWindow.admin_combo_tps = mainWindow.findChild(QComboBox, "admin_combo_tps")
    
    mainWindow.btn_home = mainWindow.findChild(QPushButton, "btn_home")
    mainWindow.btn_admin = mainWindow.findChild(QPushButton, "btn_admin")
    mainWindow.btn_save = mainWindow.findChild(QPushButton, "btn_save")
    mainWindow.btn_notice = mainWindow.findChild(QPushButton, "btn_notice")

    mainWindow.admin_btn_expend = mainWindow.findChild(QPushButton, "admin_btn_expend")


    #매개변수를 가진 버튼
    mainWindow.login_btn_mail.clicked.connect(lambda: mainWindow.openDialog("MailFunctionWindow"))
    mainWindow.login_btn_call.clicked.connect(lambda: mainWindow.openDialog("CallDialog"))

    mainWindow.btn_notice.clicked.connect(lambda: mainWindow.openDialog("NoticeDialog"))

    mainWindow.admin_btn_food.clicked.connect(lambda: mainWindow.openDialog("FoodDialog"))
    mainWindow.admin_btn_accept.clicked.connect(lambda: mainWindow.packetSender.acceptReq(mainWindow.socket))
    mainWindow.admin_btn_reject.clicked.connect(lambda: mainWindow.packetSender.rejectReq(mainWindow.socket))

    mainWindow.home_btn_groupmemberlist.clicked.connect(lambda: mainWindow.openDialog("GroupMemberListDialog"))
    mainWindow.home_btn_chatgroup.clicked.connect(lambda: mainWindow.openDialog("GroupAddDialog"))
    mainWindow.home_btn_add_member.clicked.connect(lambda: mainWindow.openDialog("MemberAddDialog"))
    mainWindow.home_listview_chatgroup.clicked.connect(lambda index: mainWindow.groupClick(index, mainWindow.groupname))

    mainWindow.admin_btn_expend.clicked.connect(lambda: mainWindow.openDialog("GrafanaDialog"))

def initialize_variable(mainWindow: QMainWindow):
    mainWindow.groupname = None
    mainWindow.groupList = []
    mainWindow.userList = []
    mainWindow.groupMemberList = []
    mainWindow.userId = None
    mainWindow.socket = None
    # mainWindow.chatGroupModel = QStringListModel(mainWindow.home_listview_chatgroup)
    # mainWindow.home_listview_chatgroup.setModel(mainWindow.chatGroupModel)
