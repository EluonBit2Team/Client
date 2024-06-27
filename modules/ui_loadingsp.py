import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt

class LoadingGif(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainUI()
        
    def mainUI(self):
        self.setObjectName("FTwindow")
        self.resize(200, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 배경을 투명하게 설정

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 150, 150))
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setObjectName("lb1")
        self.label.setScaledContents(True)
        #self.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("C:\project\Client\images\images\loader2.gif")
        self.label.setMovie(self.movie)

    

        self.startAnimation()

    # Start Animation
    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
        self.close()

    # Disable moving the window
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass
# self.loadingGif = LoadingGif()
# self.loadingGif.show()
# QTimer.singleShot(1000, self.loadingGif.stopAnimation) # 로딩 딜레이
