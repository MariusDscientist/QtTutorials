# This script explains the concept of custom signals and slots in PySide6.
# It defines a `Communicate` class with an overloaded signal `speak` that can
# emit either an integer or a string. It also shows how to connect these
# signals to a slot that is decorated to handle both data types,
# demonstrating signal/slot overloading and type-based dispatch.

import sys 
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot

class Communicate(QObject):
    #Create two new signals on the fly: one wil handle
    #int type, the other will handle the strings

    speak = Signal((int,), (str,))

    def __init__(self, parent=None):
        super().__init__(parent)

        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)
    
    #Define a new slot that receives a C 'int' or a 'str'
    #and has 'say_something' as its name

    @Slot(int)
    @Slot(str)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("This is a number: ", arg)
        elif isinstance(arg, str):
            print("This is a string: ", arg)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    someone = Communicate()

    #emit 'speak' signal with different arguments.
    #we have to specify the str as int is the default
    someone.speak[int].emit(10)
    someone.speak[str].emit("Hello everybody")