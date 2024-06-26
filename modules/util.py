import socket
import json
import struct
from modules import *
from widgets import *
from collections import OrderedDict
from PySide6.QtWidgets import QMainWindow


SERVER_ADDR = "192.168.0.253"
# SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 3335

#json type 4번은 ui_groupadddlg_function으로
TYPE_LOGIN = 2
TYPE_MESSAGE = 3
TYPE_USERLIST = 5
TYPE_GROUPLIST = 6
TYPE_EDIT_GROUP_MEMBER = 7
TYPE_ERROR = 100
TYPE_GROUPMEMBER = 11
TYPE_CHATLIST = 12
TYPE_REQ_LIST = 8
TYPE_ACCEPT_SIGNUP = 9
TYPE_ACCEPT_GROUP = 10


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
    
# class util:
#     def __init__(self, main_window):
#         self.main_window = main_window

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

def updateDisplay(self, list, type, model):
    print("updateDisplay 진입")
    model.clear()
    if type == "grouplist":
        for i in list:
            item = QStandardItem(i['groupname'])
            model.appendRow(item)
    elif type == "userlist":
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        for json_data in list:
            makeRow = json_data['dept_name'] + ' ' + \
                json_data['position_name'] + ' ' + json_data['name']
            name_column = QStandardItem(makeRow)
            id_column = QStandardItem(json_data["login_id"])
            name_column.setData(json_data, Qt.UserRole)
            row = [name_column, id_column]
            model.appendRow(row)
    elif type == "signupList":
        for json_data in list:
            makeRow = "회원가입요청     || " + json_data['login_id'] + ' ' + \
                json_data['name'] + ' ' + json_data['phone'] + ' ' + json_data['email']
            item = QStandardItem(makeRow)
            item.setData(json_data, Qt.UserRole)
            model.appendRow(item)
    elif type == "groupReqList":
        for json_data in list:
            makeRow = "그룹생성요청     || " + json_data['group_name'] + ' ' + json_data['memo']
            item = QStandardItem(makeRow)
            item.setData(json_data, Qt.UserRole)
            model.appendRow(item)
    elif type == "groupMemberList":
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        for json_data in list:
            makeRow = json_data['dept_name'] + ' ' + \
                json_data['position_name'] + ' ' + json_data['name']
            name_column = QStandardItem(makeRow)
            id_column = QStandardItem(json_data["login_id"])
            name_column.setData(json_data, Qt.UserRole)
            row = [name_column, id_column]
            model.appendRow(row) 
    elif (type == "sent") or (type == "received"):
        item = QStandardItem(list)
        item.setData(type, Qt.ItemDataRole.UserRole + 1)
        model.appendRow(item)
        self.home_listview_chatlist.scrollToBottom()

def getClickedRow(type, widget, model):
    if type == "json":
        selected_indexes = widget.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = model.itemFromIndex(index)
            json_data = item.data(Qt.UserRole)
        
        return json_data

    if type == "string":
        selected_indexes = widget.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = model.itemFromIndex(index)
            string_data = item.data(Qt.DisplayRole)
        
        return string_data
    
# def 


    
    
