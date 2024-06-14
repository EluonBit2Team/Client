import socket
import json
import struct
from modules import *
from widgets import *


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


def importUtil():
    print('import util.py')
    
# def connectSocket(addr, port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((addr, int(port)))
#         sock.setblocking(False)
#         connectionSuccessEvent()
#     except Exception:
#         connectionErrorEvent()
    

def connectionErrorEvent():
    QMessageBox.warning(None, "Error", "연결 실패")

def connectionSuccessEvent():
    QMessageBox.information(None, "Success", "연결 성공")


    
