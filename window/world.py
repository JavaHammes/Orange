#!/opt/homebrew/bin/python3


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

    def translateLine(self, x, y):
        for line in self.lines:
            line.moveLine(x, y)

    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def getWidgets(self):
        return (self.widgets)

    def addLine(self, line):
        self.lines.append(line)

    def getLines(self):
        return self.lines
