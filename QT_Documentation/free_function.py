# This script demonstrates that a Qt signal can be connected to a "free" function,
# meaning a function that is not a method of a class.
# It creates a simple QPushButton and connects its 'clicked' signal to a standalone function.

import sys 
from PySide6.QtWidgets import QApplication, QPushButton

#signals can also be connected to free functions:

def function(): 
    print("THe function has been called!")

app = QApplication()
buttom = QPushButton("Call function")
buttom.clicked.connect(function)
buttom.show()
sys.exit(app.exec())


