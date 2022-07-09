#!/opt/homebrew/bin/python3

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPoint

class RImage(QLabel):

    def __init__(self, parent, x, y, width, height, path):
        super().__init__(parent)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = path

        self.oldPos = QPoint()

        self.move(self.x, self.y)

        self.pixmap = QPixmap(path)
        self.scaled_pixmap = self.pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.setPixmap(self.scaled_pixmap)

        self.lines = list()
       
    def getPixmap(self):
        return (self.scaled_pixmap)

    def getX(self):
        return (self.x)

    def getY(self):
        return (self.y)

    def getWidth(self):
        return (self.width)

    def getHeight(self):
        return (self.height)

    def addLine(self, rline):
        self.lines.append(rline)

    def getLines(self):
        return (self.lines)
