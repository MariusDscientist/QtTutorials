# This script provides a basic example of a QPushButton in PySide6.
# It demonstrates how to create a button, connect its 'clicked' signal
# to a Python function (a "slot"), and use the @Slot decorator.

import sys 
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)

button = QPushButton("click me")
button.clicked.connect(say_hello)
button.show()

app.exec()