from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .ui_chatmemberadd import Ui_Dialog

class MemberAddDialog(QDialog, Ui_Dialog):
    def __init__(self, main_window, listModel):
        super().__init__(main_window)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main_window = main_window
        # CenterAlignDelegate를 설정하여 아이템 가운데 정렬
        self.delegate = CenterAlignDelegate()
        self.ui.dialog_listview_left.setItemDelegate(self.delegate)

        # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)
        
        
        #connect widget
        self.ui.dialog_listview_left.setModel(listModel)
        #self.ui.dialog_btn_insert.clicked.connect(self.moveItem(self.dialog_listview_left, self.dialog_listview_right))
        #self.ui.dialog_btn_delete.clicked.connect(self.deleteItem)
    
    def moveItem(list1, list2):
        pass

    

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