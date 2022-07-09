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

    def paintEvent(self, e):
        for line in self.world.getLines():
            line.paintLine()

    def mousePressEvent(self, e):
        self.mousePressPos = None
        self.rightClickPressed = False
        self.mouseLeftPressPos = None
        self.leftClickPressed = False
        if e.button() == Qt.MouseButton.RightButton:
            self.mousePressPos = e.pos()
            self.rightClickPressed = True
        elif e.button() == Qt.MouseButton.LeftButton:
            self.mouseLeftPressPos = e.pos()
            self.leftClickPressed = True

    def mouseMoveEvent(self, e):
        if self.rightClickPressed is True:
            moved = e.pos() - self.mousePressPos
            self.world.translate(int(moved.x()), int(moved.y()))
            self.mousePressPos = e.pos()
            self.repaint()
        elif self.leftClickPressed is True:
            moved = e.pos() - self.mouseLeftPressPos
            movedWidget = self.childAt(int(e.pos().x()), int(e.pos().y()))
            if movedWidget is not None:
                self.world.translateSelectedWidget(movedWidget,int(moved.x()), int(moved.y()))
            self.mouseLeftPressPos = e.pos()
            self.repaint()





            #print("global pos click: ", e.globalPosition())
            #print("local pos click: ", e.pos())
            #print("global pos image: ", self.rimage_three.mapToGlobal(self.rimage_three.pos()))
            #print("normal pos image: ", self.rimage_three.pos())
            #print("child at: ", self.childAt(int(e.globalPosition().x()), int(e.globalPosition().y())))
            #print("###########################")
