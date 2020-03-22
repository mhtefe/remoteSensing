import os
import os.path
import sys

from qgis.PyQt import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TestWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        uic.loadUi('2_test.ui', self)
        self._initUi()

        self.ui.label().setText("1")
        self.ui.obj._label.setText("2") # alike

        self.ui.pushButton().clicked.connect(self.changeLabel)

    def changeLabel(self):
        self.ui.label().setText("ehebelel")

    def _initUi(self):
        self.ui = _Ui(self)

class _Ui(object):
    def __init__(self, obj):
        self.obj = obj

    def label(self):
        assert isinstance(self.obj._label, QLabel)
        return self.obj._label

    def pushButton(self):
        assert isinstance(self.obj._pushButton, QPushButton)
        return self.obj._pushButton

app = QApplication(sys.argv)

window = TestWindow()
window.show()
window.raise_()

app.exec_()
app.deleteLater()

