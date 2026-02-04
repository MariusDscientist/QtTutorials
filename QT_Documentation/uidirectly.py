# This script demonstrates how to load a Qt Designer .ui file directly at runtime
# using the QUiLoader class. This is an alternative approach to generating
# a static Python UI file. It allows for more dynamic loading of user interfaces.

import sys 
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app =QApplication(sys.argv)

    ui_file_name = "QT_Documentation/mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not  ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())