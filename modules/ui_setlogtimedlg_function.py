from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.ui_setlogtimedlg import Ui_Dialog

class SetLogTimeDlg(QDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        current_datetime = QDateTime.currentDateTime()
        one_month_ago = current_datetime.addMonths(-1)
        
        self.ui.dialog_dateTimeEdit_start.setCalendarPopup(True)
        self.ui.dialog_dateTimeEdit_end.setCalendarPopup(True)
        
        self.ui.dialog_dateTimeEdit_start.setDateTime(one_month_ago)
        self.ui.dialog_dateTimeEdit_end.setDateTime(current_datetime)
        
        self.ui.dialog_btn_submit.clicked.connect(self.clickSubmit)
    
    def clickSubmit(self):
        self.start_time = self.ui.dialog_dateTimeEdit_start.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.end_time = self.ui.dialog_dateTimeEdit_end.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.main_window.packetSender.searchChatLog(self.main_window.socket)
        self.close_dialog()
    
    def close_dialog(self):
        self.accept()  # 다이얼로그 닫기    
        