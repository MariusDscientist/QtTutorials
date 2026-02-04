# This script demonstrates how to create a simple dialog application.
# It includes a QLineEdit for text input and a QPushButton.
# When the button is clicked, a greeting is printed to the console,
# showcasing how to connect a button's clicked signal to a slot (a function).

import sys 
from PySide6.QtWidgets import QLineEdit, QVBoxLayout ,QApplication, QDialog, QLineEdit, QPushButton

class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("My Form")

        #Create widgets
        self.edit = QLineEdit("Write my name here")
        self.buttom = QPushButton("Show Greetings")
        
        #Create layout and widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.buttom)

        #Set dialog layout
        self.setLayout(layout)
        #Add buttom signal to grettings slot
        self.buttom.clicked.connect(self.greetings)

    def greetings(self):
        print(f"Hello {self.edit.text()}")



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    form = Form()
    form.show()

    sys.exit(app.exec())