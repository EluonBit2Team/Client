import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *

class MailFunctionWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.send_mail()

    def send_mail(self):
        email_address = "example@example.com"
        subject = "제목 예시"
        body = "이메일 본문 예시"
        
        mailto_link = f"mailto:{email_address}?subject={subject}&body={body}"
        QDesktopServices.openUrl(QUrl(mailto_link))


