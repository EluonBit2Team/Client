import sys 
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtGui import QMovie 
from PyQt6.QtCore import Qt
  
  
class LoadingGif(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainUI()

    def mainUI(self):
        self.setObjectName("FTwindow")
        self.resize(320, 300)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # FramelessWindowHint 적용
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 배경을 투명하게 설정

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 250, 250))
        self.label.setMinimumSize(QtCore.QSize(250, 250))
        self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("lb1")
        self.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("loader.gif")
        self.label.setMovie(self.movie)

        self.startAnimation()

    # Start Animation
    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
  
  
