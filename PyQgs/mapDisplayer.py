import os
import os.path
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from qgis.PyQt import uic
from qgis.core import *
from qgis.gui import *

class TestWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('base_form.ui', self)
        self._initUi()

        QMainWindow.setCentralWidget(self, self.ui.centralWidget())

        self.ui.actionPan().triggered.connect(self.setPanMode)

        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapCanvas.show()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)
        self.ui.centralWidget().setLayout(layout)

        self.panTool = PanTool(self.mapCanvas)
        self.panTool.setAction(self.ui.actionPan())

    def setPanMode(self):
        self.mapCanvas.setMapTool(self.panTool)

    def loadMap(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))

        filename = os.path.join(cur_dir,
                                "data",
                                "NE1_HR_LC_SR_W_DR",
                                "NE1_HR_LC_SR_W_DR.tif")
        self.basemapLayer = QgsRasterLayer(filename, "basemap")

        QgsProject.instance().addMapLayer(self.basemapLayer)
       

        self.showVisibleMapLayers()

        self.mapCanvas.setExtent(QgsRectangle(-127.7, 24.4, -79.3, 49.1))

    def showVisibleMapLayers(self):
        layers = []
        layers.append(self.basemapLayer)
        self.mapCanvas.setLayers(layers)

    def _initUi(self):
        self.ui = _Ui(self)

class PanTool(QgsMapTool):
    def __init__(self, mapCanvas):
        QgsMapTool.__init__(self, mapCanvas)
        self.setCursor(Qt.OpenHandCursor)

    def canvasMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.canvas().panAction(event)

    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.canvas().panActionEnd(event.pos())

class _Ui(object):
    def __init__(self, obj):
        self.obj = obj

    def actionPan(self):
        assert isinstance(self.obj.actionPan, QAction)
        return self.obj.actionPan

    def centralWidget(self):
        assert isinstance(self.obj.centralWidget, QWidget)
        return self.obj.centralWidget

app = QApplication(sys.argv)
QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
QgsApplication.initQgis()

window = TestWindow()
window.show()
window.loadMap()
window.setPanMode()
window.raise_()

app.exec_()
app.deleteLater()
QgsApplication.exitQgis()

