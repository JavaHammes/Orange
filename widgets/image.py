#!/opt/homebrew/bin/python3

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class RImage(QLabel):

    def __init__(self, parent, x, y, width, height, path):
        super().__init__(parent)

        self.x = x
        self.y = y
        self.width = width
        self.heiht = height
        self.path = path

        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)

        self.setPixmap(scaled_pixmap)
       
        self.move(x, y)
