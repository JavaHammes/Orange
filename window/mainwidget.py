#!/opt/homebrew/bin/python3

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QEvent, QPoint
from PyQt6.QtGui import QCursor

from widgets.image import RImage
from widgets.line import RLine

from window.world import World

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.world = World()

        self.rimage_one = RImage(self, -700, 300, 400, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test1.png")
        self.rimage_two = RImage(self, 100, 200, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test2.png")
        self.rimage_three = RImage(self, 1000, 400, 300, 300, "/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test3.png")

        self.rline = RLine(self, self.rimage_one, self.rimage_two)
        self.rline_two = RLine(self, self.rimage_two, self.rimage_three)

        self.rimage_one.addLine(self.rline)
        self.rimage_two.addLine(self.rline)
        self.rimage_two.addLine(self.rline_two)
        self.rimage_three.addLine(self.rline_two)
        
        self.world.addWidget(self.rimage_one)
        self.world.addWidget(self.rimage_two)
        self.world.addWidget(self.rimage_three)
        self.world.addLine(self.rline)
        self.world.addLine(self.rline_two)

        self.widget_one = None
        self.widget_two = None
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, e):
        for line in self.world.getLines():
            line.paintLine()

    def mousePressEvent(self, e):
        self.mousePressPos = None
        self.middleClickPressed = False
        self.mouseRightPressPos = None
        self.rightClickPressed = False
        if e.button() == Qt.MouseButton.MiddleButton:
            self.mousePressPos = e.pos()
            self.middleClickPressed = True
        elif e.button() == Qt.MouseButton.RightButton:
            self.mouseRightPressPos = e.pos()
            self.rightClickPressed = True

    def mouseMoveEvent(self, e):
        if self.middleClickPressed is True:
            moved = e.pos() - self.mousePressPos
            self.world.translate(int(moved.x()), int(moved.y()))
            self.mousePressPos = e.pos()
            self.repaint()
        elif self.rightClickPressed is True:
            moved = e.pos() - self.mouseRightPressPos
            movedWidget = self.childAt(int(e.pos().x()), int(e.pos().y()))
            if movedWidget is not None:
                self.world.translateSelectedWidget(movedWidget,int(moved.x()), int(moved.y()))
            self.mouseRightPressPos = e.pos()
            self.repaint()

    def keyPressEvent(self, e):
        spacebar = 32
        key = e.key()
        mousePos = self.mapFromGlobal(QCursor.pos())
        child = self.childAt(int(mousePos.x()), int(mousePos.y()))
        if key == spacebar:
            if child == None:
                return

            if self.widget_one == None:
                self.widget_one = child 
            elif self.widget_two == None:
                self.widget_two = child
                newLine = RLine(self, self.widget_one, self.widget_two)
                self.world.addLine(newLine)
                self.widget_one.addLine(newLine)
                self.widget_two.addLine(newLine)
                self.widget_one = None
                self.widget_two = None
                self.repaint()
