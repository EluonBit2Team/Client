from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .ui_groupadddlg import Ui_Dialog

import socket
import json
import struct
from .send_packet import SendPacket

class GroupAddDialog(QDialog, Ui_Dialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.dialog_edit_chattitle = self.findChild(QLineEdit, "dialog_edit_chattitle")
         # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)

    def sendGroupReq(self):
        self.sock = self.main_window.socket
        self.userid = self.main_window.username
        self.groupname = self.dialog_edit_chattitle.text()
        try:
            msg = {
                "type": 4,
                "id": self.main_window.username,
                "groupname": self.groupname,
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
            
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def close_dialog(self):
        self.accept()  # 다이얼로그 닫기    

