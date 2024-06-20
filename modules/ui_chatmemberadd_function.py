from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .ui_chatmemberadd import Ui_Dialog

class MemberAddDialog(QDialog, Ui_Dialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.setWindowTitle("대화 상대 초대하기")
        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))
        self.groupname = main_window.groupname
        self.all_items = []
        # CenterAlignDelegate를 설정하여 아이템 가운데 정렬
        self.delegate = CenterAlignDelegate()
        self.ui.dialog_treeview_left.setItemDelegate(self.delegate)
        

        # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)
        
        #initialize TreeView
        self.treeview_left_model = QStandardItemModel()
        self.treeview_right_model = QStandardItemModel()
        self.treeview_right_model.setHorizontalHeaderLabels(["이름", "아이디"])
        self.ui.dialog_treeview_right.setModel(self.treeview_right_model)
        self.ui.dialog_treeview_left.setModel(self.main_window.userListModel)
        
        #connect widget
        self.ui.dialog_btn_insert.clicked.connect(self.moveItem)
        self.ui.dialog_btn_delete.clicked.connect(self.deleteItem)
        self.ui.dialog_btn_send.clicked.connect(self.makeMemberList)
    
    def moveItem(self):
        selectedIndexes = self.ui.dialog_treeview_left.selectedIndexes()
        
        if selectedIndexes:
            selectedIndex = selectedIndexes[0]
            json_data = self.main_window.userListModel.data(selectedIndex, Qt.UserRole)
            if json_data:
                print(json_data)
                displayRow = json_data['dept_name'] + ' ' + json_data['position'] + ' ' + json_data['name']
                selectedItem = QStandardItem()
                selectedItem.setData(json_data, Qt.UserRole)  # JSON 데이터를 새로운 아이템에 설정
                selectedItem.setText(displayRow)
                self.treeview_right_model.appendRow(selectedItem)
        else:
            print("아무것도 선택되지 않았습니다.")
    
    def deleteItem(self):
        selectedIndexes = self.ui.dialog_treeview_right.selectedIndexes()
        
        if selectedIndexes:
            for selectedIndex in selectedIndexes:
                self.treeview_right_model.removeRow(selectedIndex.row())
        else:
            print("아무것도 선택되지 않았습니다.")
    
    def makeMemberList(self):
        print("makeMemberList 시작됨")
        item_count = self.treeview_right_model.rowCount()
        print(item_count)
        
        for row in range(item_count):
            item = self.treeview_right_model.item(row)
            json_data = item.data(Qt.UserRole)
            name = json_data.get("id")
            self.all_items.append(name)
        
        # 모든 아이템 출력
        print("All items in list view:")
        for item in self.all_items:
            print(item)
        
        self.main_window.packetSender.reqAddGroupMember(self.main_window.socket, self.groupname, self.all_items)
        print("그룹이름: " + self.groupname)
        
        
    def printItem(self):
        # item_count = self.main_window.memberAddDialog.treeview_left_model.rowCount()
        item_count = self.treeview_right_model.rowCount()
        print(item_count)
        
        for row in range(item_count):
            item = self.treeview_right_model.item(row)
            json_data = item.data(Qt.UserRole)
            name = json_data.get("id")
            self.all_items.append(name)
        
        # 모든 아이템 출력
        print("All items in list view:")
        for item in self.all_items:
            print(item)

    def close_dialog(self):
        self.accept()  # 다이얼로그 닫기  

# 리스트 가운데 정렬 클래스
class CenterAlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

    def paint(self, painter, option, index):
        self.initStyleOption(option, index)
        painter.save()
        style = option.widget.style()
        style.drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
        painter.restore()