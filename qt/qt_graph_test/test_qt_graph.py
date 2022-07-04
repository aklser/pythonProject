import cgitb
import sys
import numpy as np
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, \
    QGridLayout, QApplication, QListView, QMainWindow
import pyqtgraph as pg
from numpy import random

from adb import adb_cpu_fps_mem


class Demo(QWidget):
    # 初始化
    def __init__(self):
        super(Demo, self).__init__()
        self.initui()
    # 布局
    def initui(self):
        self.resize(1000, 800)
        self.center()
        # pyqraph全局设置
        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # plot数据设置
        self.pw = pg.PlotWidget(self)
        self.pw2 = pg.PlotWidget(self)
        self.pw3 = pg.PlotWidget(self)
        r_symbol, r_color = self.random_item()
        self.myGDate = np.empty(3)
        self.ptr = 0
        self.plot_data = self.pw.plot(self.myGDate, pen="r", symbol=r_symbol, symbolBrush=r_color)

        # 按钮
        self.plot_btn = QPushButton('reset', self)
        self.plot_btn.clicked.connect(self.start_remake)

        # 左侧界面
        self.G_layout_2 = QGridLayout()
        self.listView = QListView()
        self.listView2 = QListView()

        slm = QStandardItemModel()
        self.qList = [{"serial_n": "xghmozaiwgcylr7p", "state": "device"},
                      {"serial_n": "xghmozaiwgcylr7p", "state": "device"},
                      {"serial_n": "xghmozaiwgcylr7p", "state": "device"}
                      ]
        for i in self.qList:
            item = QStandardItem(i["serial_n"] + ":    " + i["state"])
            slm.appendRow(item)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.l_clicked)

        self.listView2.setModel(slm)
        self.listView2.clicked.connect(self.l_clicked)

        self.G_layout_2.setRowStretch(0, 1)
        self.G_layout_2.setRowStretch(1, 1)
        self.G_layout_2.setColumnStretch(0, 1)
        self.G_layout_2.addWidget(self.listView)
        self.G_layout_2.addWidget(self.listView2)
        # 布局
        self.G_layout = QGridLayout()
        self.V_layout = QVBoxLayout()

        # 右侧三图表与按钮
        self.V_layout.addWidget(self.pw)
        self.V_layout.addWidget(self.pw2)
        self.V_layout.addWidget(self.pw3)
        self.V_layout.addWidget(self.plot_btn)

        # 右侧与左侧的位置与比例
        self.G_layout.addLayout(self.G_layout_2, 0, 0, -1, 1)
        self.G_layout.addLayout(self.V_layout, 0, 1)
        self.G_layout.setColumnStretch(0, 1)
        self.G_layout.setColumnStretch(1, 4)
        self.setLayout(self.G_layout)

    # 应用居中
    def center(self):
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()

        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    # 设置图表中点的颜色与形状
    def plot_slot(self):
        x, y, r_symbol, r_color = self.random_item()
        self.plot_data.setData(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)

    # 开始/重置按钮功能
    def start_remake(self):
        print("开始！")
        self.timer_update()

    # 图表点位图标颜色与形状随机
    def random_item(self):
        # x = np.random.normal(size=1000)
        # y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
        return r_symbol, r_color

    # 左侧点击事件
    def l_clicked(self, qModelIndex):
        print(self.qList[qModelIndex.row()])
        # print(qModelIndex)

    # 更新第一个表数据
    def update_mydate(self):
        self.data_all = adb_cpu_fps_mem.do_fps_line("com.tencent.tim")
        print(self.data_all)
        print(self.data_all['xghmozaiwgcylr7p'][0])
        if not self.data_all:
            print("请打开gpu呈现模式中的adb或打开任意应用")
            self.data_all['xghmozaiwgcylr7p'][0] = 0
        print(self.data_all['xghmozaiwgcylr7p'][0])
        self.myGDate[self.ptr] = self.data_all['xghmozaiwgcylr7p'][0]
        if self.ptr + 1 >= self.myGDate.shape[0]:
            tmp = self.myGDate
            self.myGDate = np.empty(self.myGDate.shape[0] * 2)
            self.myGDate[:tmp.shape[0]] = tmp
        self.plot_data.setData(self.myGDate[:self.ptr + 1])
        self.ptr += 1

    # 每秒更新
    def timer_update(self):
        timer = pg.QtCore.QTimer(self)
        timer.timeout.connect(self.update_mydate)
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    # cgitb.enable()
    sys.exit(app.exec())
