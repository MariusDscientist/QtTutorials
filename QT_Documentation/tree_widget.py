# This script demonstrates the use of QTreeWidget to display hierarchical data.
# It creates a tree structure from a Python dictionary, where dictionary keys
# are top-level items (e.g., project names) and values are their children (e.g., file names).
# The script also shows how to set column headers.

import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

app = QApplication(sys.argv)

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values: 
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value,ext])
        item.addChild(child)
    items.append(item)
tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec())