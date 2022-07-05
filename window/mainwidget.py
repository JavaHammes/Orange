#!/opt/homebrew/bin/python3

from PyQt6.QtWidgets import QWidget

from widgets.image import RImage
from widgets.line import RLine

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.widgets = list()
        self.initUI()

    def initUI(self):
        rimage_one = RImage(self, 1000, 400, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")
        self.widgets.append(rimage_one)
        
        rimage_two = RImage(self, 100, 200, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")
        self.widgets.append(rimage_two)

        self.rline = RLine(self, rimage_one, rimage_two)
        self.rline.calculateMidPoint(rimage_one)

    def paintEvent(self, e):
        self.rline.paintLine()
