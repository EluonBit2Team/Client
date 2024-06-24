import socket
import json
import struct
from modules import *
from widgets import *
from PySide6.QtWidgets import QMainWindow


SERVER_ADDR = "192.168.0.253"
# SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 3335
TYPE_LOGIN = 2
TYPE_MESSAGE = 0
TYPE_USERLIST = 5
TYPE_GROUPLIST = 6
TYPE_ERROR = 100
TYPE_GROUPMEMBER = 11
TYPE_CHATLIST = 12
TYPE_ACCEPT_LIST = 8
TYPE_ACCEPT_SIGNUP = 9



class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()
        messageType = index.data(Qt.ItemDataRole.UserRole + 1)

        if messageType == "sent":
            option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        else:
            option.displayAlignment = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter

        text = index.data(Qt.ItemDataRole.DisplayRole)
        painter.drawText(option.rect, option.displayAlignment, text)
        painter.restore()
        
def connectSocket(QMainWindow, addr, port):
        try:
            print(f"Connecting to {addr}:{port}")
            QMainWindow.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            QMainWindow.socket.settimeout(5)
            QMainWindow.socket.connect((addr, port))
            QMainWindow.socket.setblocking(False)
            connectionSuccessEvent()
        except socket.error as e:
            print(f"Socket connection error: {e}")
            connectionErrorEvent()

def handleSendButtonClick(self):
    QCoreApplication.processEvents()  # 프로세스 이벤트를 처리하여 UI 업데이트
        
    # 클릭 시 아이콘 변경
    self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334 - 복사본.png'))
    self.home_btn_chatlist_send.setIconSize(QSize(41, 41))
    QThread.msleep(50) # 전송버튼 sleep
        
    # 원래 아이콘으로 복원
    self.home_btn_chatlist_send.setIcon(QIcon(':/images/images/images/free-icon-send-button-12439334.png'))
    self.home_btn_chatlist_send.setIconSize(QSize(41, 41))


def connectionErrorEvent():
    QMessageBox.warning(None, "Error", "연결 실패")

def connectionSuccessEvent():
    QMessageBox.information(None, "Success", "연결 성공")

    
