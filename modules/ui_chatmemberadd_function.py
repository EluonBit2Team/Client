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
        self.in_member = []
        self.out_member = []
        # CenterAlignDelegate를 설정하여 아이템 가운데 정렬
        self.delegate = CenterAlignDelegate()
        self.ui.dialog_treeview_left.setItemDelegate(self.delegate)
        

        # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)
        
        #initialize TreeView
        self.treeview_left_model = QStandardItemModel()
        self.ui.dialog_treeview_left.setModel(self.main_window.userListModel)
        self.treeview_left_model.setHorizontalHeaderLabels(["이름", "아이디"])
        
        self.treeview_right_model = QStandardItemModel()
        self.ui.dialog_treeview_right.setModel(self.treeview_right_model)
        self.treeview_right_model.setHorizontalHeaderLabels(["이름", "아이디"])
       
        #connect widget
        self.ui.dialog_btn_insert.clicked.connect(self.moveItem)
        self.ui.dialog_btn_delete.clicked.connect(self.deleteItem)
        self.ui.dialog_btn_send.clicked.connect(lambda: self.main_window.packetSender.sendEditedMember(self.main_window.socket))
        self.ui.dialog_btn_send.clicked.connect(self.close_dialog)
        
    def moveItem(self):
        selectedIndexes = self.ui.dialog_treeview_left.selectedIndexes()
        
        if selectedIndexes:
            selectedIndex = selectedIndexes[0]
            json_data = self.main_window.userListModel.data(selectedIndex, Qt.UserRole)
            if json_data:
                makeRow = json_data['dept_name'] + ' ' + json_data['position_name'] + ' ' + json_data['name']
                name_column = QStandardItem(makeRow)
                id_column = QStandardItem(json_data["login_id"])
                name_column.setData(json_data, Qt.UserRole)
                row = [name_column, id_column]
                self.treeview_right_model.appendRow(row)
                self.in_member.append(json_data["login_id"])
                print(self.in_member)
        else:
            print("아무것도 선택되지 않았습니다.")
    
    def deleteItem(self):
        selectedIndexes = self.ui.dialog_treeview_right.selectedIndexes()
        if selectedIndexes:
            selectedIndex = selectedIndexes[0]
            json_data = self.treeview_right_model.data(selectedIndex, Qt.UserRole)
            self.treeview_right_model.removeRow(selectedIndex.row())
            self.out_member.append(json_data["login_id"])
        else:
            print("아무것도 선택되지 않았습니다.")
            
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