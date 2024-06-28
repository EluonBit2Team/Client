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
TYPE_SIGNUP_REQ = 1
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
TYPE_EDIT_USERINFO = 13
TYPE_GROUP_CHAT_REQ = 14
TYPE_GROUPDELETE_REQ = 15


class CustomDelegate(QStyledItemDelegate):
    # def init
    def paint(self, painter, option, index):
        painter.save()
        messageSender = index.data(Qt.ItemDataRole.UserRole + 1)

        if messageSender == "me":
            option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        else:
            option.displayAlignment = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter

        text = index.data(Qt.ItemDataRole.DisplayRole)
        painter.drawText(option.rect, option.displayAlignment, '  ' + text + '  ')
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

def updateDisplay(mainWindow: QMainWindow, data_list, type, model):
    print("updateDisplay 진입")
    if type == "grouplist":
        model.clear()
        for i in data_list:
            item = QStandardItem(i['groupname'])
            model.appendRow(item)
    elif type == "userlist":
        model.clear()
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        for json_data in data_list:
            print(json_data)
            makeRow = json_data['dept_name'] + ' ' + \
                json_data['position_name'] + ' ' + json_data['name']
            name_column = QStandardItem(makeRow)
            id_column = QStandardItem(json_data["login_id"])
            name_column.setData(json_data, Qt.UserRole)
            row = [name_column, id_column]
            model.appendRow(row)
    elif type == "reqList":
        signup_type = 'login_id'
        group_type = 'group_name'
        model.clear()
        for json_data in data_list:
            if signup_type in json_data:
                makeRow = "회원가입요청     || " + json_data['login_id'] + ' ' + \
                    json_data['name'] + ' ' + json_data['phone'] + ' ' + json_data['email']
                item = QStandardItem(makeRow)
                item.setData(json_data, Qt.UserRole)
                model.appendRow(item)
            if group_type in json_data:
                makeRow = "그룹생성요청     || " + json_data['group_name'] + ' ' + json_data['memo']
                item = QStandardItem(makeRow)
                item.setData(json_data, Qt.UserRole)
                model.appendRow(item)
    elif type == "groupMemberList":
        model.clear()
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        for json_data in data_list:
            makeRow = json_data['dept_name'] + ' ' + \
                json_data['position_name'] + ' ' + json_data['name']
            name_column = QStandardItem(makeRow)
            id_column = QStandardItem(json_data["login_id"])
            name_column.setData(json_data, Qt.UserRole)
            row = [name_column, id_column]
            model.appendRow(row)
    elif type == "clickedGroup":
        print(data_list)
        model.clear()
        for json_data in data_list:
            print(json_data)
            name = json_data['login_id']
            message = json_data['text']
            if mainWindow.userId == name:
                sentUser = "me"
            else:
                sentUser = "other"
            row_count = model.rowCount()
            if row_count<1:
                item = QStandardItem(name)
                item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                model.appendRow(item)
                
                item = QStandardItem(message)
                item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                item.setData(json_data, Qt.UserRole)
                model.appendRow(item)
            else:
                last_index = model.index(row_count - 1, 0)
                last_item = model.itemFromIndex(last_index)
                row_json_data = last_item.data(Qt.UserRole)
                print(row_json_data)
                lastSender = row_json_data['login_id']
                print(lastSender)
                if lastSender == name:
                    item = QStandardItem(message)
                    item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                    item.setData(json_data, Qt.UserRole)
                    model.appendRow(item)
                else:
                    item = QStandardItem(name)
                    item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                    model.appendRow(item)
                    
                    item = QStandardItem(message)
                    item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                    item.setData(json_data, Qt.UserRole)
                    model.appendRow(item)
                
                mainWindow.home_listview_chatlist.scrollToBottom()
            
            mainWindow.home_listview_chatlist.scrollToBottom()
    
    elif type == "receivedChat":
        name = data_list['login_id']
        message = data_list['text']
        print("now my id: " + mainWindow.userId)
        print("received massage id: " + name)
        if mainWindow.userId == name:
            sentUser = "me"
        else:
            sentUser = "other"
        print("sentUser: " + sentUser)
        row_count = model.rowCount()
        if row_count<1:
            item = QStandardItem(name)
            item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
            model.appendRow(item)
            
            item = QStandardItem(message)
            item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
            item.setData(data_list, Qt.UserRole)
            model.appendRow(item)
        else:
            print("row_count가 2 이상이라 else로 넘어감")
            last_index = model.index(row_count - 1, 0)
            last_item = model.itemFromIndex(last_index)
            row_json_data = last_item.data(Qt.UserRole)
            lastSender = row_json_data['login_id']
            print(lastSender)
            print(data_list)
            if lastSender == name:
                print("lastSender == name")
                item = QStandardItem(message)
                item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                item.setData(data_list, Qt.UserRole)
                model.appendRow(item)
            else:
                item = QStandardItem(name)
                item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                model.appendRow(item)
                
                item = QStandardItem(message)
                item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
                item.setData(data_list, Qt.UserRole)
                model.appendRow(item)
            
            mainWindow.home_listview_chatlist.scrollToBottom()
        
        mainWindow.home_listview_chatlist.scrollToBottom()

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

def groupClick(mainWindow: QMainWindow, listname, index):
    if listname == "useredit_treeview_userlist":
        item_json = index.data(Qt.UserRole)
        mainWindow.useredit_edit_id.setText(item_json['login_id'])
    elif listname == "home_listview_chatgroup":
        item_text = index.data(Qt.DisplayRole)
        mainWindow.nowGroupName = item_text
        mainWindow.packetSender.reqGroupChat(mainWindow.socket)
        print(item_text)

def sortUserInfo(var, name):
    if name == "dept":
        if var == "부서를 선택하세요.":
            return 999
        elif var == "1팀":
            return 1
        elif var == "2팀":
            return 2
        elif var == "3팀":
            return 3
        else:
            return 4
    
    elif name == "pos":
        if var == "직급을 선택하세요.":
            return 999
        elif var == "회장":
            return 1
        elif var == "사장":
            return 2
        elif var == "차장":
            return 3
        elif var == "과장":
            return 4
        elif var == "대리":
            return 5
        elif var == "사원":
            return 6
    
    elif name == "role":
        if var == "역할을 선택하세요.":
            return 999
        else:
            return int(var)
    
    elif name == "tps":
        if var == "tps를 선택하세요.":
            return 999
        else:
            return int(var)
        
    
    

# class AnimationClass:
#     def __init__(self, main_window):
#         self.main_window = main_window

    # def switchPage(self, currentPage, nextPage):
    #     self.animateTransition(self.main_window, currentPage, nextPage)
    #     self.stackedWidget.setCurrentWidget(nextPage)

    # def animateTransition(self, fromIndex, toIndex):
    #         currentWidget = self.stackedWidget.widget(fromIndex)
    #         nextWidget = self.stackedWidget.widget(toIndex)

    #         currentRect = self.stackedWidget.geometry()
    #         width = currentRect.width()

    #         # 다음 위젯의 초기 위치를 스택 위젯의 오른쪽으로 설정
    #         nextWidget.setGeometry(currentRect.x() + width, currentRect.y(), width, currentRect.height())

    #         # 현재 위젯을 왼쪽으로 밀어내는 애니메이션
    #         self.currentAnimation = QPropertyAnimation(currentWidget, b"geometry")
    #         self.currentAnimation.setDuration(500)
    #         self.currentAnimation.setStartValue(currentRect)
    #         self.currentAnimation.setEndValue(QRect(currentRect.x() - width, currentRect.y(), width, currentRect.height()))
    #         self.currentAnimation.setEasingCurve(QEasingCurve.InOutQuad)

    #         # 다음 위젯을 제자리에 맞추는 애니메이션
    #         self.nextAnimation = QPropertyAnimation(nextWidget, b"geometry")
    #         self.nextAnimation.setDuration(500)
    #         self.nextAnimation.setStartValue(nextWidget.geometry())
    #         self.nextAnimation.setEndValue(currentRect)
    #         self.nextAnimation.setEasingCurve(QEasingCurve.InOutQuad)

    #         # 애니메이션 시작
    #         self.currentAnimation.start()
    #         self.nextAnimation.start()

def setPage(self, nextPage):
    self.stackedWidget.setCurrentWidget(nextPage)

def animateTransition(self, currentPage, nextPage, onFinished):
    parentRect = currentPage.geometry()
    width = parentRect.width()

    # 다음 위젯의 초기 위치를 스택 위젯의 오른쪽으로 설정
    nextPage.setGeometry(parentRect.x() + width, parentRect.y(), width, parentRect.height())
    
    # 현재 위젯을 왼쪽으로 밀어내는 애니메이션
    self.currentAnimation = QPropertyAnimation(currentPage, b"geometry")
    self.currentAnimation.setDuration(500)
    self.currentAnimation.setStartValue(parentRect)
    self.currentAnimation.setEndValue(QRect(parentRect.x() - width, parentRect.y(), width, parentRect.height()))
    self.currentAnimation.setEasingCurve(QEasingCurve.InOutSine)

    # 다음 위젯을 제자리에 맞추는 애니메이션
    self.nextAnimation = QPropertyAnimation(nextPage, b"geometry")
    self.nextAnimation.setDuration(500)
    self.nextAnimation.setStartValue(QRect(parentRect.x() + width, parentRect.y(), width, parentRect.height()))
    self.nextAnimation.setEndValue(parentRect)
    self.nextAnimation.setEasingCurve(QEasingCurve.InOutSine)
    
    # 애니메이션 그룹 생성
    self.animationGroup = QParallelAnimationGroup()
    self.animationGroup.addAnimation(self.nextAnimation)
    self.animationGroup.addAnimation(self.currentAnimation)
    
    # 애니메이션 그룹이 끝났을 때 호출될 콜백 설정
    self.animationGroup.finished.connect(lambda: onFinished(self, nextPage))
    
    # 애니메이션 그룹 시작
    self.animationGroup.start()

def animateTransitionBack(self, currentPage, nextPage, onFinished):
    parentRect = currentPage.geometry()
    width = parentRect.width()

    # 다음 위젯의 초기 위치를 스택 위젯의 왼쪽으로 설정
    nextPage.setGeometry(parentRect.x() - width, parentRect.y(), width, parentRect.height())
    
    # 현재 위젯을 오른쪽으로 밀어내는 애니메이션
    self.currentAnimation = QPropertyAnimation(currentPage, b"geometry")
    self.currentAnimation.setDuration(500)
    self.currentAnimation.setStartValue(parentRect)
    self.currentAnimation.setEndValue(QRect(parentRect.x() + width, parentRect.y(), width, parentRect.height()))
    self.currentAnimation.setEasingCurve(QEasingCurve.InOutSine)

    # 다음 위젯을 제자리에 맞추는 애니메이션
    self.nextAnimation = QPropertyAnimation(nextPage, b"geometry")
    self.nextAnimation.setDuration(500)
    self.nextAnimation.setStartValue(QRect(parentRect.x() - width, parentRect.y(), width, parentRect.height()))
    self.nextAnimation.setEndValue(parentRect)
    self.nextAnimation.setEasingCurve(QEasingCurve.InOutSine)
    
    # 애니메이션 그룹을 생성하고 두 애니메이션을 추가
    self.animationGroup = QParallelAnimationGroup()
    self.animationGroup.addAnimation(self.nextAnimation)
    self.animationGroup.addAnimation(self.currentAnimation)
    self.animationGroup.finished.connect(lambda: onFinished(self, nextPage))

    # 애니메이션 그룹 시작
    self.animationGroup.start()
    


    
    
