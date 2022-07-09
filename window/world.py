#!/opt/homebrew/bin/python3

from PyQt6.QtCore import QPoint

class World():

    def __init__(self, widgets, lines):
        self.widgets = widgets
        self.lines = lines

    def __init__(self):
        self.widgets = list()
        self.lines = list()

    def translate(self, x, y):
        for widget in self.widgets:
            widget.move(widget.pos().x() + x, widget.pos().y() + y) 

        for line in self.lines:
            line.moveLine(x, y)

    def translateSelectedWidget(self, widget, x, y):
           widget.move(widget.pos().x() + x, widget.pos().y() + y) 
           lines = widget.getLines()
           for line in lines:
               line.moveEndPoint(self.calculateMidPoint(widget))

    def calculateMidPoint(self, widget):
        x = widget.pos().x()
        y = widget.pos().y()
        w = widget.getWidth()
        h = widget.getHeight()

        mid_x = x + w/2
        mid_y = y + h/2

        return (QPoint(mid_x, mid_y))

    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def getWidgets(self):
        return (self.widgets)

    def addLine(self, line):
        self.lines.append(line)

    def getLines(self):
        return self.lines
