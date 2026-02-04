# This script illustrates how to use a Python class generated from a Qt Designer .ui file.
# It imports the `Ui_MainWindow` class from the `ui_mainwindow.py` file
# and uses it to construct the user interface for the main window.
# This is a common pattern for separating UI design from application logic.

import sys 
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())