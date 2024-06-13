from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

# 알림 버튼 클릭시 표출 다이얼로그
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("알림")
        self.setGeometry(100, 100, 600, 400)

        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))

        # Set dialog background color using RGB
        self.setStyleSheet("background-color: rgb(40, 44, 52);")  # 원하는 RGB 값으로 변경

        # Dialog layout and widgets
        layout = QVBoxLayout()  # 여기서 레이아웃을 먼저 선언합니다.
        
        self.label = QLabel("This is a custom notice dialog.")
        layout.addWidget(self.label)

        # QListView 설정
        self.listView = QListView()
        self.model = QStandardItemModel()
        
        # 리스트에 항목 추가
        items = ["Item 1", "Item 2", "Item 3", "Item 4"]
        for item in items:
            listItem = QStandardItem(item)
            self.model.appendRow(listItem)
        
        self.listView.setModel(self.model)
        layout.addWidget(self.listView)
        
        self.okButton = QPushButton("나가기")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)
        
        self.setLayout(layout)  # 레이아웃을 다이얼로그에 설정합니다.
        
        # window 바로 앞에 위치 시킴
        if parent:
            parent_rect = parent.geometry()
            self_rect = self.geometry()
            x = parent_rect.x() + (parent_rect.width() - self_rect.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self_rect.height()) // 2
            self.move(x, y)
