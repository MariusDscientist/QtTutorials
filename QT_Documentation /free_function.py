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


