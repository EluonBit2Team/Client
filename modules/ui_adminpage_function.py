# grafana_dashboard.py
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

import sys

class GrafanaDashboard:
    def __init__(self, parent=None):
        self.parent = parent

    def setup_dashboard(self):
        # 이미 생성된 QWebEngineView 위젯을 찾기
        self.browser = self.parent.findChild(QWebEngineView, "admin_webEn_acmember")
        if self.browser:
            # Grafana 대시보드 URL 설정
            grafana_url = "http://192.168.0.145:3000/d/cdp7caqtun94wd/message-log?orgId=1"
            self.browser.setUrl(QUrl(grafana_url))
            
            # 페이지가 로드되면 자격 증명을 입력하고 로그인
            self.browser.loadFinished.connect(self.on_load_finished)

            # 일정 간격으로 페이지 새로고침
            self.refresh_timer = QTimer(self.browser)
            self.refresh_timer.timeout.connect(self.browser.reload)
            #self.refresh_timer.start(1000)  # 1초마다 새로고침

    def on_load_finished(self):
        # 약간의 지연을 추가하여 페이지가 완전히 로드된 후에 JavaScript 코드 실행
        QTimer.singleShot(10000, self.execute_login_script)

    def execute_login_script(self):
        # 로그인 페이지에서 자격 증명을 입력하고 로그인 버튼을 클릭하는 JavaScript 코드
        login_script = """
        (function() {
            var userInput = document.getElementsByName('user')[0];
            var passwordInput = document.getElementsByName('password')[0];
            var submitButton = document.querySelector('button[type="submit"]');
            if (userInput && passwordInput && submitButton) {
                userInput.value = 'admin';
                passwordInput.value = '12345';
                submitButton.click();
                return 'Login script executed';
            } else {
                return 'Login elements not found';
            }
        })();
        """
        self.browser.page().runJavaScript(login_script, self.on_script_executed)

    def on_script_executed(self, result):
        print(result)  # JavaScript 코드의 실행 결과 출력

