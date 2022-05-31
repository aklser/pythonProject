import cgitb
import sys
import numpy as np
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QApplication, QListView
import pyqtgraph as pg
from numpy import random


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.initui()

    def initui(self):
        self.setGeometry(0, 0, 2000, 1000)
        # pyqraph全局设置
        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # plot数据设置
        self.pw = pg.PlotWidget(self)
        self.pw2 = pg.PlotWidget(self)
        self.pw3 = pg.PlotWidget(self)
        # x, y, r_symbol, r_color = self.random_item()
        # self.plot_data = self.pw.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)

        # 按钮
        self.plot_btn = QPushButton('开始', self)
        self.plot_btn.clicked.connect(self.plot_slot)

        # 左界面
        self.G_layout_2 = QGridLayout()
        self.listView = QListView()
        self.listView2 = QListView()
        #
        slm = QStandardItemModel()
        self.qList = [{"serial_n": "7HX5T19924012747", "state": "device"},
                      {"serial_n": "7HX5T19924012747", "state": "device"},
                      {"serial_n": "7HX5T19924012747", "state": "device"}]
        for i in self.qList:
            item = QStandardItem(i["serial_n"] + ":       " + i["state"])
            slm.appendRow(item)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.clicked)
        #
        self.listView2.setModel(slm)
        self.listView2.clicked.connect(self.clicked)
        #
        self.G_layout_2.setRowStretch(0, 1)
        self.G_layout_2.setRowStretch(1, 1)
        self.G_layout_2.setColumnStretch(0, 1)
        self.G_layout_2.addWidget(self.listView)
        self.G_layout_2.addWidget(self.listView2)
        # # 布局
        self.G_layout = QGridLayout()
        self.V_layout = QVBoxLayout()
        #
        self.V_layout.addWidget(self.pw)
        self.V_layout.addWidget(self.pw2)
        self.V_layout.addWidget(self.pw3)
        self.V_layout.addWidget(self.plot_btn)
        #
        #
        self.G_layout.addLayout(self.G_layout_2, 0, 0, -1, 1)
        self.G_layout.addLayout(self.V_layout, 0, 1)
        self.G_layout.setColumnStretch(0, 1)
        self.G_layout.setColumnStretch(1, 4)
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

    def clicked(self, qModelIndex):
        print(self.qList[qModelIndex.row()])
        print(qModelIndex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()

    cgitb.enable()
    sys.exit(app.exec())
