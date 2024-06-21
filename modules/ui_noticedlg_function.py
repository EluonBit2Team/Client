from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *
from modules.ui_noticedlg import Ui_Dialog  # 변환된 UI 파일을 임포트합니다.

# 빈 다이얼로그
class CustomDialogNotice(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()  # UI 클래스 인스턴스를 생성합니다.
        self.ui.setupUi(self)  # UI 설정을 다이얼로그에 적용합니다.
        
        self.setWindowTitle("알림")
        self.setGeometry(100, 100, 640, 470)

        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))

        # 다이얼로그를 부모 창의 중앙에 위치시킴
        if parent:
            parent_rect = parent.geometry()
            self_rect = self.geometry()
            x = parent_rect.x() + (parent_rect.width() - self_rect.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self_rect.height()) // 2
            self.move(x, y)
            
        # dialog_btn_exit 버튼을 눌렀을 때 다이얼로그를 닫도록 연결
        self.ui.dialog_btn_exit.clicked.connect(self.close_dialog)

    def close_dialog(self):
        self.accept()  # 다이얼로그 닫기

