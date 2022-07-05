#!/opt/homebrew/bin/python3

from PyQt6.QtGui import QPainter, QPainterPath, QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtCore import Qt

from widgets.image import RImage
from widgets.line import RLine

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.widgets = list()
        self.initUI()

    def initUI(self):
        #rimage = RImage(self, 500, 400, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")
        #self.widgets.append(rimage)
        
        #rimage = RImage(self, 100, 200, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")
        #self.widgets.append(rimage)

        self.rline = RLine(self, 0, 0)

    def paintEvent(self, e):
        self.rline.paintLine()
