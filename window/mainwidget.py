#!/opt/homebrew/bin/python3

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QEvent, QPoint

from widgets.image import RImage
from widgets.line import RLine

from window.world import World

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.world = World()
        self.initUI()

    def initUI(self):
        self.rimage_one = RImage(self, 1000, 400, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")

        self.rimage_two = RImage(self, 100, 200, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")

        self.rline = RLine(self, self.rimage_one, self.rimage_two)
        
        self.world.addWidget(self.rimage_one)
        self.world.addWidget(self.rimage_two)
        self.world.addWidget(self.rline)

    def paintEvent(self, e):
        self.rline.paintLine()

    def mousePressEvent(self, e):
        self.mousePressPos = None
        self.mouseMovePos = None
        self.rightClickPressed = False
        if e.button() == Qt.MouseButton.RightButton:
            self.mousePressPos = e.globalPosition()
            self.mouseMovePos = e.globalPosition()
            self.rightClickPressed = True

        super(MainWidget, self).mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.rightClickPressed is True:
            moved = e.globalPosition() - self.mousePressPos
            self.world.translate(int(moved.x()), int(moved.y()))
            self.mousePressPos = e.globalPosition()
        super(MainWidget, self).mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if self.mousePressPos is not None:
            moved = e.globalPosition() - self.mousePressPos
            self.world.translate(int(moved.x()), int(moved.y()))

        super(MainWidget, self).mouseReleaseEvent(e)
   
