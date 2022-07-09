#!/opt/homebrew/bin/python3

from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine, QPoint
from PyQt6.QtWidgets import QWidget

from widgets.image import RImage

class RLine(QWidget):

    def __init__(self, parent, widget_one, widget_two):
        super().__init__(parent)
        
        self.parent = parent
        
        self.widget_one = widget_one
        self.widget_two = widget_two

        self.point_one = self.calculateMidPoint(self.widget_one)
        self.point_two = self.calculateMidPoint(self.widget_two)

        self.line = QLine(self.point_one, self.point_two)
        

    def paintLine(self):
        painter = QPainter()
        painter.begin(self.parent)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawLine(self.line)
        painter.end()

    def calculateMidPoint(self, widget):
        x = widget.pos().x()
        y = widget.pos().y()
        w = widget.getWidth()
        h = widget.getHeight()
        
        mid_x = x + w/2 
        mid_y = y + h/2

        return (QPoint(mid_x, mid_y))

    def moveLine(self, x, y):
        self.line.translate(x,y)
        self.point_one = self.line.p1()
        self.point_two = self.line.p2()

    def moveEndPoint(self, mid_point):
        mid_point_one = self.calculateMidPoint(self.widget_one)
        mid_point_two = self.calculateMidPoint(self.widget_two)
        if self.point_one != mid_point_one:
            self.point_one = mid_point
        elif self.point_two != mid_point_two:
            self.point_two = mid_point

        self.line = QLine(self.point_one, self.point_two)

    def getLine(self):
        return (self.line)
