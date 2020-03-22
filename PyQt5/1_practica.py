from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys, os

def pushed():
    print("clicked...")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Practica")

    label = QLabel(win)
    label.setText("label prac")
    label.move(50, 50)

    b1 = QPushButton(win)
    b1.setText("prac")
    b1.clicked.connect(pushed)

    win.show()
    sys.exit(app.exec_())


window()