# This is a fundamental "Hello, World!" example using PySide6.
# It demonstrates creating a simple application with a QLabel widget.
# The label's text is styled using HTML formatting to change its color and size.

import sys 
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
app.exec()

