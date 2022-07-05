#!/opt/homebrew/bin/python3

from PyQt6.QtGui import QPainter, QPainterPath, QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtCore import Qt


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

    def addImage(self, imagePath):
        pixmap = QPixmap(imagePath)
        scaled_pixmap = pixmap.scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        

        label = QLabel(self)
        label.setPixmap(scaled_pixmap)



    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):

        path = QPainterPath()
        path.moveTo(30,30)
        path.cubicTo(30,30,200,350,350,30)

        qp.drawPath(path)

