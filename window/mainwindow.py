#!/opt/homebrew/bin/python3

import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication, QTextEdit
from PyQt6.QtGui import QAction, QIcon

from window.mainwidget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        mainWidget = MainWidget()
        self.setCentralWidget(mainWidget)

        self.setGeometry(300,300,350,250)
        self.setMinimumSize(1400,800)
        self.setWindowTitle("Orange")
        self.setStyleSheet("background-color: rgb(100,100,100);")
        self.show()
