from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.ui_grafana import Ui_Dialog
from modules.ui_adminpage_function import *

class GrafanaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()  # UI 클래스 인스턴스를 생성합니다.
        self.ui.setupUi(self)  # UI 설정을 다이얼로그에 적용합니다.
        
        self.setWindowTitle("그라파나 대시보드")
        self.setGeometry(100, 100, 1081, 701)

        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))
        
        # 다이얼로그를 부모 창의 중앙에 위치시킴
        if parent:
            parent_rect = parent.geometry()
            self_rect = self.geometry()
            x = parent_rect.x() + (parent_rect.width() - self_rect.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self_rect.height()) // 2
            self.move(x, y)

        grafana_dashboard = GrafanaDashboard(self)
        grafana_dashboard.setup_dashboard()    
        
