#!/opt/homebrew/bin/python3

from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine, QPoint

from widgets.image import RImage

class RLine():

    def __init__(self, parent, widget_one, widget_two):
        
        self.parent = parent
        
        self.widget_one = widget_one
        self.widget_two = widget_two

        self.point_one = self.calculateMidPoint(self.widget_one)
        self.point_two = self.calculateMidPoint(self.widget_two)

        self.line = QLine(self.point_one, self.point_two)
        

    def paintLine(self):
        painter = QPainter()
        painter.begin(self.parent)
        painter.drawLine(self.line)
        painter.end()

    def calculateMidPoint(self, widget):
        x = widget.getX()
        y = widget.getY()
        w = widget.getWidth()
        h = widget.getHeight()
        
        print(x , y, w, h)

        mid_x = x + w/2 
        mid_y = y + h/2

        print(QPoint(mid_x, mid_y))
        return (QPoint(mid_x, mid_y))

