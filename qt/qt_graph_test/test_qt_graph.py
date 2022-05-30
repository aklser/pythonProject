import cgitb
import sys
import random
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setGeometry(0, 0, 2000, 1000)

        # pyqraph全局设置
        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # plot数据设置
        self.pw = pg.PlotWidget(self)
        self.pw2 = pg.PlotWidget(self)
        self.pw3 = pg.PlotWidget(self)
        x, y, r_symbol, r_color = self.random_item()
        self.plot_data = self.pw.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)

        # 按钮
        self.plot_btn = QPushButton('reset', self)
        self.plot_btn.clicked.connect(self.plot_slot)

        # l界面
        self.V_layout_2 = QVBoxLayout()
        self.model = QStandardItemModel(6, 2)
        self.model.setHorizontalHeaderLabels(["序列号", "状态"])

        for row in range(6):
            for col in range(2):
                self.model.setItem(row, col, QStandardItem("1"))
        self.tabletV = QTableView()
        self.tabletV.setModel(self.model)
        self.V_layout_2.addWidget(self.tabletV)

        # 布局
        self.G_layout = QGridLayout()
        self.V_layout = QVBoxLayout()

        self.V_layout.addWidget(self.pw)
        self.V_layout.addWidget(self.pw2)
        self.V_layout.addWidget(self.pw3)
        self.V_layout.addWidget(self.plot_btn)

        #
        self.G_layout.addLayout(self.V_layout_2, 0, 0, -1, 1)
        self.G_layout.addLayout(self.V_layout, 0, 1)
        self.setLayout(self.G_layout)

    def plot_slot(self):
        x, y, r_symbol, r_color = self.random_item()
        self.plot_data.setData(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)

    def random_item(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
        return x, y, r_symbol, r_color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    cgitb.enable()
    sys.exit(app.exec())
