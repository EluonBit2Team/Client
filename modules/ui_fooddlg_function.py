from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import math
from .ui_fooddlg import Ui_Dialog

class RouletteWidget(QWidget):

    
    angleChanged = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._angle = 0
        self.animation = QPropertyAnimation(self, b"angle")
        self.animation.setDuration(4000)
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.setWindowTitle("음식 룰렛 돌리기")
        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))
        # 각 섹션에 표시할 텍스트 목록
        self.sections = ["한식", "중식", "일식", "양식", "분식", "편의점"]

    @Property(int)
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        painter.translate(rect.center())
        painter.rotate(self._angle)
        painter.translate(-rect.center())

        # 룰렛 그리기
        colors = [Qt.red, Qt.green, Qt.blue, Qt.yellow, Qt.cyan, Qt.magenta]
        num_sections = len(colors)
        angle_per_section = 360 / num_sections

        for i, color in enumerate(colors):
            painter.setBrush(color)
            painter.drawPie(rect, int(i * angle_per_section * 16), int(angle_per_section * 16))

        # 텍스트 그리기
        painter.setPen(Qt.black)  # 텍스트 색상 설정
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)

        radius = rect.width() / 2  # 반지름 계산
        text_radius = radius * 0.7  # 텍스트를 표시할 반지름 (조금 더 안쪽)

        for i, text in enumerate(self.sections):
            angle = (i * angle_per_section + angle_per_section / 2) - self._angle
            radian = angle * math.pi / 180  # 각도를 라디안으로 변환
            x = rect.center().x() + text_radius * math.cos(radian) - painter.fontMetrics().horizontalAdvance(text) / 2
            y = rect.center().y() - text_radius * math.sin(radian) + painter.fontMetrics().ascent() / 2
            painter.drawText(QPointF(x, y), text)

    def startSpin(self):
        start_angle = self.angle
        end_angle = start_angle + 360 * 5 + (360 / 6) * QRandomGenerator.global_().bounded(6)
        self.animation.setStartValue(start_angle)
        self.animation.setEndValue(end_angle)
        self.animation.start()

# 빈 다이얼로그
class CustomDialog_food(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()  # UI 클래스 인스턴스를 생성합니다.
        self.ui.setupUi(self)  # UI 설정을 다이얼로그에 적용합니다.

        self.setWindowTitle("오늘의 점심 고르기")
        self.setGeometry(100, 100, 640, 470)

        self.setWindowIcon(QIcon(':/images/images/images/logo.png'))

        # 룰렛을 다이얼로그의 중앙에 배치
        self.roulette = RouletteWidget(self)
        self.roulette.setGeometry((self.width() - 250) // 2, (self.height() - 250) // 2, 250, 250)

        # 시작하기 버튼
        self.ui.dialog_btn_start.clicked.connect(self.roulette.startSpin)

        # 다이얼로그를 부모 창의 중앙에 위치시킴
        if parent:
            parent_rect = parent.geometry()
            self_rect = self.geometry()
            x = parent_rect.x() + (parent_rect.width() - self_rect.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self_rect.height()) // 2
            self.move(x, y)

# 예제 실행 코드
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dlg = CustomDialog_food()
    dlg.show()
    sys.exit(app.exec())
