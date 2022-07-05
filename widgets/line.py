#!/opt/homebrew/bin/python3

from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine

class RLine():

    def __init__(self, parent, widget_one, widget_two):
        
        self.parent = parent

        self.line = QLine(0,0,300,300)

    def paintLine(self):
        print("Trying to draw line")
        painter = QPainter()
        painter.begin(self.parent)
        painter.drawLine(self.line)
        painter.end()


