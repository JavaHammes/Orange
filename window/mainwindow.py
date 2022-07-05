#!/opt/homebrew/bin/python3

import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication, QTextEdit
from PyQt6.QtGui import QAction, QIcon

from window.mainwidget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        mainWidget = MainWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.addImage("/Users/alexander/Desktop/Dokumente/Meine Programme/osint/save/pictures/test.png")

        self.setGeometry(300,300,350,250)
        self.setMinimumSize(300,300)
        self.setWindowTitle("Orange")
        self.show()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

