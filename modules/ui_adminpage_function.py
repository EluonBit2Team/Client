from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *


class AcceptFunctionWindow(QMainWindow):
    def __init__(self, main_window):
        self.main_window = main_window


