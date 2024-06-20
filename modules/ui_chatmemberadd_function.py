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
        self.ui.dialog_listview_left.setModel(listModel)