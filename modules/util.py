import socket
import json
import struct
from modules import *
from widgets import *
from collections import OrderedDict
from PySide6.QtWidgets import QMainWindow
import threading

SERVER_ADDR = "192.168.0.149"
# SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 3334

#json type 4번은 ui_groupadddlg_function으로
TYPE_CONNECTION = 0
TYPE_SIGNUP_REQ = 1
TYPE_LOGIN = 2
TYPE_MESSAGE = 3
TYPE_USERLIST = 5
TYPE_GROUPLIST = 6
TYPE_EDIT_GROUP_MEMBER = 7
TYPE_ACCEPT_SIGNUP = 9
TYPE_ERROR = 100
TYPE_GROUPMEMBER = 11
TYPE_REQ_LIST = 8
TYPE_ACCEPT_GROUP = 10
TYPE_EDIT_USERINFO = 13
TYPE_GROUP_CHAT_REQ = 14
TYPE_LOG_REQ = 16
TYPE_GROUPDELETE_REQ = 15
TYPE_REALTIME_REQ = 17
TYPE_DM_SEND = 18
TYPE_DM_LOG = 19
TYPE_LEAVE_GROUP = 20
TYPE_CURRENT_USERLIST = 22
TYPE_ERROR_DUP_LOGIN = 102
TYPE_USERLOG_REQ = 21
TYPE_ONLINE_REQ = 300
TYPE_SERVERERR_REQ = 301


class CustomDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    # 보낸사람에 따라 각각 정렬
    def paint(self, painter, option, index):
        painter.save()
        messageSender = index.data(Qt.ItemDataRole.UserRole + 1)
        rowType = index.data(Qt.ItemDataRole.UserRole + 2)
        text = index.data(Qt.ItemDataRole.DisplayRole)
        formatted_text = self.format_text(text, 30)

        if messageSender == "me":
            option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            bubble_color = QColor(31, 181, 71)  # green
            text_color = Qt.white
        else:
            option.displayAlignment = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
            bubble_color = QColor(14, 84, 204)  # blue
            text_color = Qt.white
        
        rect = option.rect.adjusted(10, -5, -10, 5)
        
        if rowType == "name":
            font = QFont()
            font.setPointSize(10)  # Set font size to 14px
            painter.setFont(font)
            painter.drawText(rect, option.displayAlignment, formatted_text)
        else:
            font = QFont()
            font.setPointSize(12)
            painter.setFont(font)
            text_rect = painter.boundingRect(option.rect, Qt.TextWordWrap, formatted_text)
            bubble_rect = text_rect.adjusted(-10, -5, 10, 5)
            if messageSender == "me":
                bubble_rect.moveRight(option.rect.right() - 15)
                bubble_rect.setLeft(max(bubble_rect.left(), option.rect.left() + 15))
            else:
                bubble_rect.moveLeft(option.rect.left() + 15)
                bubble_rect.setRight(min(bubble_rect.right(), option.rect.right() - 15))
            painter.setBrush(bubble_color)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(bubble_rect, 10, 10)
            painter.setPen(QPen(text_color))
            painter.drawText(bubble_rect, Qt.AlignCenter, formatted_text)
            painter.restore()
            return

        # Text alignment options
        text_option = QTextOption()
        text_option.setAlignment(option.displayAlignment)
        
        painter.setPen(QPen(text_color))
        # painter.drawText(rect, formatted_text, text_option)
        painter.restore()
        
    def format_text(self, text, line_length):
        lines = []
        for i in range(0, len(text), line_length):
            lines.append(text[i:i+line_length])
        return '\n'.join(lines)

    def sizeHint(self, option, index):
        text = index.data(Qt.ItemDataRole.DisplayRole)
        formatted_text = self.format_text(text, 30)
        lines = formatted_text.split('\n')
        padding_between_lines = 8  # 각 줄 사이의 기본적인 패딩
        first_line_padding = 10  # 첫 번째 줄의 추가 패딩
        last_line_padding = 10  # 마지막 줄의 추가 패딩

        line_heights = []
    
        for i, line in enumerate(lines):
            if len(line) <= 30 and len(lines) == 1:
                line_heights.append(option.fontMetrics.height() + first_line_padding + last_line_padding)
            elif i == 0:
                line_heights.append(option.fontMetrics.height() + first_line_padding)
            elif i == len(lines) - 1:
                line_heights.append(option.fontMetrics.height() + last_line_padding)
            else:
                line_heights.append(option.fontMetrics.height() + padding_between_lines)
        height = sum(line_heights)
        width = min(option.rect.width(), 600)
        return QSize(width, height)
    
    
# class util:
#     def __init__(self, main_window):
#         self.main_window = main_window

class ClientSession:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.userId = None
        self.main_window.userRole = None
    
    def loginSession(self, userId, userRole):
        self.main_window.userId = userId
        self.main_window.userRole = userRole

    def logoutSession(self):
        self.main_window.userId = None
        self.main_window.userRole = None


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

def groupListNoti(groupname, model, view):
    for row in range(model.rowCount()):
        item = model.item(row)
        if item.text() == groupname:
            current_color = item.background().color()
            item.setData(current_color, Qt.UserRole + 2)
            item.setBackground(QBrush(QColor(255, 255, 0, 100)))
            view.viewport().update()

def userListNoti(userId, model, view):
    id_column_index = 1 
    name_column_index = 0
    for row in range(model.rowCount()):
        item = model.item(row, id_column_index)
        name = model.item(row, name_column_index)
        if item.text() == userId:
            print("아이템 텍스트: " + item.text())
            current_color = item.background().color()
            name.setData(current_color, Qt.UserRole + 2)
            name.setBackground(QBrush(QColor(255, 255, 0, 100)))
            view.viewport().update()
            
def groupListUpdate(data, model):
    for json_data in data:
        item = QStandardItem(json_data['groupname'])
        item.setData(json_data, Qt.UserRole)
        model.appendRow(item)

def addNameRow(sentUser, name, model):
    rowType="name"
    item = QStandardItem(name)
    item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
    item.setData(rowType, Qt.ItemDataRole.UserRole + 2)
    model.appendRow(item)

def addTextRow(sentUser, message, json_data, model):
    rowType="text"
    item = QStandardItem(message)
    item.setData(sentUser, Qt.ItemDataRole.UserRole + 1)
    item.setData(rowType, Qt.ItemDataRole.UserRole + 2)
    item.setData(json_data, Qt.UserRole)
    model.appendRow(item)

def updateDisplay(mainWindow: QMainWindow, data_list, data_type, model):
    print("updateDisplay 진입")
    if data_type == "grouplist":
        model.clear()
        groupListUpdate(data_list, model)
    
    elif data_type == "userlist":
        print("userList 진입함")
        model.clear()
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        mainWindow.home_treeview_userlist.setColumnWidth(0, 200)
        print("로그인한 유저목록")
        print(mainWindow.loginUserList)
        for json_data in data_list:
            if json_data['login_id'] in mainWindow.loginUserList:
                makeRow = "🟢" + json_data['dept_name'] + ' ' + \
                    json_data['position_name'] + ' ' + json_data['name']
                name_column = QStandardItem(makeRow)
                id_column = QStandardItem(json_data["login_id"])
                name_column.setData(json_data, Qt.UserRole)
                row = [name_column, id_column]
                model.appendRow(row)
            else:
                makeRow = "🔴" + json_data['dept_name'] + ' ' + \
                    json_data['position_name'] + ' ' + json_data['name']
                name_column = QStandardItem(makeRow)
                id_column = QStandardItem(json_data["login_id"])
                name_column.setData(json_data, Qt.UserRole)
                row = [name_column, id_column]
                model.appendRow(row)
        mainWindow.home_treeview_userlist.viewport().update()
        print("유저목록 업데이트 완료")
    elif data_type == "reqList":
        if not data_list:
            model.clear()
            return
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
    elif data_type == "groupMemberList":
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

    elif data_type == "serverLogList":
        print("serverLogList 진입")
        if not data_list:
            model.clear()
            return
        
        model.clear()
        model.setHorizontalHeaderLabels(["날짜", "UP TIME", "DOWN TIME"])
        for json_data in data_list:
            if 'uptime' in json_data and 'downtime' in json_data:
                uptime = json_data['uptime']
                downtime = json_data['downtime']
                
                
                date_column = QStandardItem(uptime.split(' ')[0])  # 날짜 부분만 추출
                uptime_column = QStandardItem(uptime)
                downtime_column = QStandardItem(downtime)
                
                date_column.setData(json_data, Qt.UserRole)
                
                row = [date_column, uptime_column, downtime_column]
                    
                model.appendRow(row)
            else:
                print("Error: 'uptime' or 'downtime' key not found in", json_data)

    elif data_type == "userLogList":
        print("userLogList 진입")
        if not data_list:
            model.clear()
            return
            
        model.clear()
        model.setHorizontalHeaderLabels(["접속된 아이디", "접속 시간", "접속 종료 시간"])
        for json_data in data_list:
            if json_data['logout_time'] is not None:
                loginid = json_data['login_id']
                logintime = json_data['login_time']
                logouttime = json_data['logout_time']
                if logouttime == "NULL":
                    loginNow = "접속중"
                    id_column = QStandardItem(loginid)
                    login_column = QStandardItem(logintime.split(' ')[0])  # 날짜 부분만 추출
                    logout_column = QStandardItem(loginNow)
                    
                    # 배경색 빨간색으로 설정
                    # for column in [id_column, login_column, logout_column]:
                    #     column.setBackground(Qt.red)
                    
                    id_column.setData(json_data, Qt.UserRole)
                    
                    row = [id_column, login_column, logout_column]
                    # 리스트의 가장 위에 추가
                    model.appendRow(row)
                else:
                    id_column = QStandardItem(loginid)
                    login_column = QStandardItem(logintime.split(' ')[0])  # 날짜 부분만 추출
                    logout_column = QStandardItem(logouttime)

                    id_column.setData(json_data, Qt.UserRole)
                    
                    row = [id_column, login_column, logout_column]

                    model.appendRow(row)
            else:
                print("Error: 'loginid' or 'login_time' or 'login_column' key not found in", json_data)

    elif data_type in ["realtimememList", "realtimeloginList", "realtimetpsList"]:
        model.clear()
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        
        mem = data_list['mem']
        usercnt = data_list['login_user_cnt']
        tps = data_list['tps']
        
        if data_type == "realtimememList":
            item = QStandardItem(f"{mem}% / 100%    램 용량: 8GB")
            item.setFont(font)
            model.appendRow(item)

        elif data_type == "realtimeloginList":
            item = QStandardItem(f"{usercnt}명 접속")
            item.setFont(font)
            model.appendRow(item)

        elif data_type == "realtimetpsList":
            item = QStandardItem(f"{tps} TPS")
            item.setFont(font)
            model.appendRow(item)
    
    elif data_type == "clickedGroup":
        print("clickedgroup 진입")
        model.clear()
        for json_data in data_list:
            login_id = json_data['login_id']
            name = mainWindow.userList[login_id]
            message = json_data['text']
            if mainWindow.userId == login_id:
                sentUser = "me"
            else:
                sentUser = "other"
            row_count = model.rowCount()
            if row_count<2:
                addNameRow(sentUser, name, model)
                addTextRow(sentUser, message, json_data, model)
            else:
                last_index = model.index(row_count - 1, 0)
                last_item = model.itemFromIndex(last_index)
                row_json_data = last_item.data(Qt.UserRole)
                lastSender = row_json_data['login_id']
                if lastSender == login_id:
                    addTextRow(sentUser, message, json_data, model)
                else:
                    addNameRow(sentUser, name, model)
                    addTextRow(sentUser, message, json_data, model)
        mainWindow.home_listview_chatlist.scrollToBottom()
    
    elif data_type=="clickedUser":
        model.clear()
        for json_data in data_list:
            login_id = json_data['sender_login_id']
            name = mainWindow.userList[login_id]
            message = json_data['text']
            if mainWindow.userId == login_id:
                sentUser = "me"
            else:
                sentUser = "other"
            row_count = model.rowCount()
            if row_count<2:
                addNameRow(sentUser, name, model)
                addTextRow(sentUser, message, json_data, model)
            else:
                last_index = model.index(row_count - 1, 0)
                last_item = model.itemFromIndex(last_index)
                row_json_data = last_item.data(Qt.UserRole)
                lastSender = row_json_data['sender_login_id']
                if lastSender == login_id:
                    addTextRow(sentUser, message, json_data, model)
                else:
                    addNameRow(sentUser, name, model)
                    addTextRow(sentUser, message, json_data, model)
        mainWindow.home_listview_chatlist.scrollToBottom()
    
    elif data_type == "receivedChat":
        login_id = data_list['login_id']
        name = mainWindow.userList[login_id]
        message = data_list['text']
        if mainWindow.userId == login_id:
            sentUser = "me"
        else:
            sentUser = "other"
        print("sentUser: " + sentUser)
        row_count = model.rowCount()
        if row_count<1:
            addNameRow(sentUser, name, model)
            addTextRow(sentUser, message, data_list, model)
        else:
            last_index = model.index(row_count - 1, 0)
            last_item = model.itemFromIndex(last_index)
            row_json_data = last_item.data(Qt.UserRole)
            lastSender = row_json_data['login_id']
            if lastSender == login_id:
                addTextRow(sentUser, message, data_list, model)
            else:
                addNameRow(sentUser, name, model)
                addTextRow(sentUser, message, data_list, model)
        mainWindow.home_listview_chatlist.scrollToBottom()
    
    elif data_type == "receivedDm":
        login_id = data_list['sender_login_id']
        name = mainWindow.userList[login_id]
        message = data_list['text']
        if mainWindow.userId == login_id:
            sentUser = "me"
        else:
            sentUser = "other"
        row_count = model.rowCount()
        if row_count<1:
            addNameRow(sentUser, name, model)
            addTextRow(sentUser, message, data_list, model)
        else:
            last_index = model.index(row_count - 1, 0)
            last_item = model.itemFromIndex(last_index)
            row_json_data = last_item.data(Qt.UserRole)
            lastSender = row_json_data['sender_login_id']
            if lastSender == login_id:
                addTextRow(sentUser, message, data_list, model)
            else:
                addNameRow(sentUser, name, model)
                addTextRow(sentUser, message, data_list, model)
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

def updateStartTime(date):
    # 선택한 날짜를 'yyyy-MM-dd HH:mm:ss.zzz' 형식으로 변환
    start_time = date.toString("yyyy-MM-dd") + " 00:00:00.000"
    
    # end_time을 start_time 다음 날로 설정
    end_date = date.addDays(1)
    end_time = end_date.toString("yyyy-MM-dd") + " 00:00:00.000"
    
    print(f'start_time: {start_time}, end_time: {end_time}')
    
    return start_time, end_time

def groupClick(mainWindow: QMainWindow, listname, index):
    if listname == "useredit_treeview_userlist":
        item_json = index.data(Qt.UserRole)
        mainWindow.nowClickedRow = item_json
        mainWindow.useredit_edit_id.setText(item_json['login_id'])
        mainWindow.home_listview_chatgroup.clearSelection()
        mainWindow.sendTarget = "user"
    elif listname == "home_listview_chatgroup":
        print("채팅그룹 클릭함")
        mainWindow.listMode = "chat"
        mainWindow.home_btn_return_chat.hide()
        mainWindow.home_btn_search_chat.show()
        mainWindow.home_btn_groupmemberlist.show()
        mainWindow.home_btn_add_member.show()
        item = mainWindow.groupListModel.itemFromIndex(index)
        item_json = index.data(Qt.UserRole)
        # item_text = index.data(Qt.DisplayRole)
        mainWindow.nowGroupName = item_json['groupname']
        mainWindow.home_label_chatlist_title.setText(mainWindow.nowGroupName)
        mainWindow.nowClickedRow = item_json
        mainWindow.packetSender.reqGroupChat(mainWindow.socket)
        if index.data(Qt.UserRole + 2):
            color_data = index.data(Qt.UserRole + 2)
            if color_data:
                item.setBackground(QBrush(QColor(31, 35, 41)))
            else:
                print("컬러데이터가 없어서 else로 빠짐")
                item.setBackground(QBrush(QColor(Qt.transparent)))
        mainWindow.useredit_treeview_userlist.clearSelection()
        mainWindow.sendTarget = "group"
    elif listname == "home_treeview_userlist":
        mainWindow.listMode = "chat"
        mainWindow.home_btn_search_chat.show()
        mainWindow.home_btn_return_chat.hide()
        mainWindow.home_btn_groupmemberlist.hide()
        mainWindow.home_btn_add_member.hide()
        item = mainWindow.userListModel.itemFromIndex(index)
        item_json = index.data(Qt.UserRole)
        if item_json['login_id'] == mainWindow.userId:
            mainWindow.home_label_chatlist_title.setText("나와 대화 하기")
        else:
            mainWindow.home_label_chatlist_title.setText(item_json['name'] + "님 과의 대화")
        mainWindow.nowClickedRow = item_json
        mainWindow.packetSender.reqDm(mainWindow.socket)
        if index.data(Qt.UserRole + 2):
            color_data = index.data(Qt.UserRole + 2)
            if color_data:
                item.setBackground(QBrush(QColor(31, 35, 41)))
            else:
                item.setBackground(QBrush(QColor(Qt.transparent)))
        mainWindow.home_listview_chatgroup.clearSelection()
        mainWindow.sendTarget = "user"

def sortUserInfo(var, name):
    if name == "dept":
        if var == "부서를 선택하세요":
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
        if var == "직급을 선택하세요":
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
        if var == "역할을 선택하세요":
            return 999
        else:
            return int(var)
    
    elif name == "tps":
        if var == "tps를 선택하세요":
            return 999
        else:
            return int(var)
    
def returnChat(mainWindow: QMainWindow, json_data):
    mainWindow.listMode = "chat"
    if json_data['groupname']:
        mainWindow.packetSender.reqGroupChat(mainWindow.socket)
    
    mainWindow.home_btn_return_chat.hide()
    
def removeDuplicate(list1, list2):
    # 집합을 사용하여 중복 요소 찾기
    set1 = set(list1)
    set2 = set(list2)
    
    # 중복 요소 찾기
    duplicates = set1.intersection(set2)
    
    # 중복 요소를 양쪽 리스트에서 제거
    list1 = [item for item in list1 if item not in duplicates]
    list2 = [item for item in list2 if item not in duplicates]
    
    return list1, list2


def try_connect(mainWindow: QMainWindow):
    connect_thread = threading.Thread(target=mainWindow.packetSender.connectSocket, args=(mainWindow.socket,))
    connect_thread.daemon = True
    connect_thread.start()

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





    
    