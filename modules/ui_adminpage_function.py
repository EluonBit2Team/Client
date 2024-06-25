# grafana_dashboard.py
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GrafanaDashboard:
    def __init__(self, parent=None):
        self.parent = parent

    def setup_dashboard(self):
        # 이미 생성된 QWebEngineView 위젯을 찾기
        self.browser = self.parent.findChild(QWebEngineView, "admin_webEn_expendgraf")
        if self.browser:
            # Grafana 대시보드 URL 설정
            grafana_url = "http://192.168.0.145:3000/d/cdp7caqtun94wd/message-log?orgId=1"
            self.browser.setUrl(QUrl(grafana_url))
        
            # 일정 간격으로 페이지 새로고침
            self.refresh_timer = QTimer(self.browser)
            #self.refresh_timer.start(1000)  # 1초마다 새로고침


