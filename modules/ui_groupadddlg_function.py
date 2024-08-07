from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .ui_groupadddlg import Ui_Dialog
import json
import struct

class GroupAddDialog(QDialog, Ui_Dialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.dialog_edit_chattitle = self.findChild(QLineEdit, "dialog_edit_chattitle")
        self.dialog_edit_issue = self.findChild(QLineEdit, "dialog_edit_issue")
         # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)
        self.setWindowTitle("채팅 그룹 추가")
        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))
    def sendGroupReq(self):
        self.sock = self.main_window.socket
        self.userId = self.main_window.userId
        self.groupname = self.dialog_edit_chattitle.text()
        self.message = self.dialog_edit_issue.text()
        try:
            msg = {
                "type": 4,
                "login_id": self.userId,
                "groupname": self.groupname,
                "message": self.userId + ' ' + self.message
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
            self.close_dialog()
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def close_dialog(self):
        self.dialog_edit_chattitle.clear()
        self.dialog_edit_issue.clear()
        self.accept()  # 다이얼로그 닫기    

