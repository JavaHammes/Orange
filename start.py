import sys
from PyQt6.QtWidgets import QApplication
from window.mainwindow import MainWindow 

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
