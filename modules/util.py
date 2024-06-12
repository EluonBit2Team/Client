import socket
import json
import struct
from modules import *
from widgets import *

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


    
