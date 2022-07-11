#!/opt/homebrew/bin/python3

import sys
from os.path import exists

from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication, QTextEdit
from PyQt6.QtGui import QAction, QIcon

from window.mainwidget import MainWidget
from others.save import Save

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.save = Save()
        self.filepath = self.save.convertToRelativePath("../save/mainwidget.obj")

        #self.mainWidget = None
        #if exists(self.filepath):
        print(self.save.loadObjectFromFile(self.filepath))
        print(exists(self.filepath))
        #else:
        self.mainWidget = MainWidget()


        self.setCentralWidget(self.mainWidget)

        self.setGeometry(300,300,350,250)
        self.setMinimumSize(1400,800)
        self.setWindowTitle("Orange")
        self.setStyleSheet("background-color: rgb(100,100,100);")
        self.show()

    def closeEvent(self, e):
       self.save.writeObjectToFile(self.mainWidget, self.filepath) 
