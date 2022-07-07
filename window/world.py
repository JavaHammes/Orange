#!/opt/homebrew/bin/python3


class World():

    def __init__(self, widgets):
        self.widgets = widgets

    def __init__(self):
        self.widgets = list()

    def translate(self, x, y):
        for widget in self.widgets:
            widget.move(widget.pos().x() + x, widget.pos().y() + y) 

    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def getWidgets(self):
        return (self.widgets)
