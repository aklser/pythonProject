import cgitb
import sys
from random import random

import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
import pyqtgraph as pg


class demo(QWidget):
    def __init__(self):
        super(demo, self).__init__()
        self.initui()

    def initui(self):
        self.setGeometry(0, 0, 600, 600)

        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.g = pg.PlotWidget(self)

        self.V_layout = QVBoxLayout()
        self.V_layout.addWidget(self.g)
        self.setLayout(self.V_layout)
        self.show()


if __name__ == "__name__":
    cgitb.enable()
    app = QApplication(sys.argv)
    ex = demo()
    sys.exit(app.exec())
