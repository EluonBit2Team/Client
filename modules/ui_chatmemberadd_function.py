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
        
        
        #connect widget
        self.ui.dialog_listview_left.setModel(listModel)
        # self.ui.dialog_btn_insert.clicked.connect(self.moveItem(self.dialog_listview_left, self.dialog_listview_right))
        # self.ui.dialog_btn_delete.clicked.connect(self.deleteItem)
    
    def moveItem(list1, list2):
        pass