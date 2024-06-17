import socket
import json
import struct
from modules import *
from widgets import *
from PySide6.QtWidgets import QMainWindow


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

def connectionErrorEvent():
    QMessageBox.warning(None, "Error", "연결 실패")

def connectionSuccessEvent():
    QMessageBox.information(None, "Success", "연결 성공")


    
