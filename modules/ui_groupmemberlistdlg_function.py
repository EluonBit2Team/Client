from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.ui_groupmemberlistdlg import Ui_Dialog

class GroupMemberListDialog(QDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.ui = Ui_Dialog()  # UI 클래스 인스턴스를 생성합니다.
        self.ui.setupUi(self)  # UI 설정을 다이얼로그에 적용합니다.
        
        self.setWindowTitle("채팅방 대화 상대")
        self.setGeometry(100, 100, 640, 470)

        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))
        
        # 다이얼로그를 부모 창의 중앙에 위치시킴
        if main_window:
            parent_rect = main_window.geometry()
            self_rect = self.geometry()
            x = parent_rect.x() + (parent_rect.width() - self_rect.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self_rect.height()) // 2
            self.move(x, y)
        
        self.groupname = main_window.groupname
            
        # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)
        
        self.groupMemberModel = QStandardItemModel(self.ui.dialog_treeview_groupmemberlist)
        self.ui.dialog_treeview_groupmemberlist.setModel(self.groupMemberModel)
        self.groupMemberModel.setHorizontalHeaderLabels(["이름", "아이디"])
        
    def close_dialog(self):
        self.groupMemberModel.clear()
        self.accept()  # 다이얼로그 닫기
    
    def updateDisplay(self, list, model):
        model.setHorizontalHeaderLabels(["이름", "아이디"])
        # for 
        for json_data in list:
            makeRow = json_data['dept_name'] + ' ' + json_data['position_name'] + ' ' + json_data['name']
            name_column = QStandardItem(makeRow)
            id_column = QStandardItem(json_data["login_id"])
            name_column.setData(json_data, Qt.UserRole)
            row=[name_column, id_column]
            model.appendRow(row)