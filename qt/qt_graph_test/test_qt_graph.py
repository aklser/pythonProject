import cgitb
import sys
import numpy as np
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, \
    QGridLayout, QApplication, QListView, QMainWindow
import pyqtgraph as pg
from numpy import random
from pyqtgraph import PlotWidget

from qt.qt_graph_test import adb_fps_cpu_mem_flow, adb_packages_list_3


class Demo(QWidget):
    # 初始化
    def __init__(self):
        super(Demo, self).__init__()
        self.initui()
        self.ser_num = ""
        self.app_name = ""
        self.upstream = 0
        self.downstream = 0

    # 布局
    def initui(self):
        self.resize(1000, 800)
        self.center()
        # pyqraph全局设置
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # plot数据设置

        self.pw = PlotWidget(self, title="fps")
        self.pw2 = PlotWidget(self, title="memory")
        self.pw3 = PlotWidget(self, title="flow")
        self.pw4 = PlotWidget(self, title="cpu")
        self.pw.addLegend()
        self.pw2.addLegend()
        self.pw3.addLegend()
        self.pw4.addLegend()
        self.pw.setLabel("left", "帧率")
        self.pw2.setLabel("left", "内存(M)")
        self.pw3.setLabel("left", "流量(KB)")
        self.pw4.setLabel("left", "cpu占比(%)")
        r_symbol, r_color = self.random_item()
        r_symbol2, r_color2 = self.random_item()
        self.arr_init = np.empty(1)
        self.arr_init[0] = 0
        self.myGDate = self.arr_init
        self.myGDate2 = self.arr_init
        self.myGDate3 = self.arr_init
        self.myGDate3_2 = self.arr_init
        self.myGDate4 = self.arr_init
        self.ptr = 0
        self.ptr2 = 0
        self.ptr3 = 0
        self.ptr3_2 = 0
        self.ptr4 = 0
        self.plot_data = self.pw.plot(self.myGDate, pen="r", symbol=r_symbol, symbolBrush=r_color, name="fps")
        self.plot_data2 = self.pw2.plot(self.myGDate2, pen="r", symbol=r_symbol, symbolBrush=r_color, name="mem")
        self.plot_data3 = self.pw3.plot(self.myGDate3, pen="r", symbol=r_symbol, symbolBrush=r_color, name="down")
        self.plot_data3_2 = self.pw3.plot(self.myGDate3_2, pen="r", symbol=r_symbol2, symbolBrush=r_color2, fillLevel=0,
                                          fillBrush=(255, 255, 255, 30), name='up')
        self.plot_data4 = self.pw4.plot(self.myGDate4, pen="r", symbol=r_symbol, symbolBrush=r_color, name="cpu")

        # 按钮
        self.plot_btn = QPushButton('reset', self)
        self.plot_btn.clicked.connect(self.start_btn)

        # 左侧界面
        self.G_layout_2 = QGridLayout()
        self.listView = QListView()
        self.listView2 = QListView()

        self.slm = QStandardItemModel()
        self.slm2 = QStandardItemModel()
        self.qList = adb_packages_list_3.adb_devices_info()
        self.qList2 = ""
        for index, item in self.qList.items():
            i = QStandardItem(item)
            self.slm.appendRow(i)
        self.slm2.appendRow(QStandardItem("请先选择设备"))
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.l_clicked)

        self.listView2.setModel(self.slm2)
        self.listView2.clicked.connect(self.l_clicked2)

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
        self.V_layout.addWidget(self.pw4)
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

    # 开始按钮功能
    def start_btn(self):
        print("开始！")
        self.timer_update_fps()
        self.timer_update_mem()
        self.timer_update_flow()
        self.timer_update_cpu()

    # 停止按钮功能
    def stop_btn(self):
        print("stop")

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
        self.ser_num = self.qList[qModelIndex.row()]
        self.slm2.removeRow(0)
        self.qList2 = adb_packages_list_3.adb_packageslist_3_info(self.ser_num)
        for index, item in self.qList2.items():
            i = QStandardItem(item)
            self.slm2.appendRow(i)

    def l_clicked2(self, qModelIndex):
        print(self.qList2[qModelIndex.row()])
        self.app_name = self.qList2[qModelIndex.row()]

    def update_fps(self):
        self.data_fps = adb_fps_cpu_mem_flow.fps_info_one(self.ser_num, self.app_name)
        print(self.data_fps)
        print(self.data_fps[self.ser_num][0])
        if not self.data_fps:
            print("请打开gpu呈现模式中的adb或打开任意应用")
            self.data_fps[self.ser_num][0] = 0
        print(self.data_fps[self.ser_num][0])
        self.myGDate[self.ptr] = self.data_fps[self.ser_num][0]
        if self.ptr + 1 >= self.myGDate.shape[0]:
            tmp = self.myGDate
            self.myGDate = np.empty(self.myGDate.shape[0] * 2)
            self.myGDate[:tmp.shape[0]] = tmp
        self.plot_data.setData(self.myGDate[:self.ptr + 1])
        self.ptr += 1

    def update_memory(self):
        self.data_memory = adb_fps_cpu_mem_flow.mem_info_one(self.ser_num, self.app_name)
        print(self.data_memory)
        print(self.data_memory[self.ser_num][0])
        if not self.data_memory:
            print("请打开gpu呈现模式中的adb或打开任意应用")
            self.data_memory[self.ser_num][0] = 0
        print(self.data_memory[self.ser_num][0])
        self.myGDate2[self.ptr2] = self.data_memory[self.ser_num][0]
        if self.ptr2 + 1 >= self.myGDate2.shape[0]:
            tmp = self.myGDate2
            self.myGDate2 = np.empty(self.myGDate2.shape[0] * 2)
            self.myGDate2[:tmp.shape[0]] = tmp
        self.plot_data2.setData(self.myGDate2[:self.ptr2 + 1])
        self.ptr2 += 1

    def update_flow(self):
        self.data_flow = adb_fps_cpu_mem_flow.flow_info_one(self.ser_num, self.app_name)
        print(self.data_flow)
        print(self.data_flow[self.ser_num][0])

        self.myGDate3[self.ptr3] = self.data_flow[self.ser_num][0] - self.downstream
        self.myGDate3_2[self.ptr3_2] = self.data_flow[self.ser_num][1] - self.upstream
        self.downstream = self.data_flow[self.ser_num][0]
        self.upstream = self.data_flow[self.ser_num][1]
        self.myGDate3[0] = 0
        self.myGDate3_2[0] = 0
        if self.ptr3 + 1 >= self.myGDate3.shape[0]:
            tmp = self.myGDate3
            tmp2 = self.myGDate3_2
            self.myGDate3 = np.empty(self.myGDate3.shape[0] * 2)
            self.myGDate3_2 = np.empty(self.myGDate3_2.shape[0] * 2)

            self.myGDate3[:tmp.shape[0]] = tmp
            self.myGDate3_2[:tmp.shape[0]] = tmp2

        self.plot_data3.setData(self.myGDate3[:self.ptr3 + 1])
        self.plot_data3_2.setData(self.myGDate3_2[:self.ptr3_2 + 1])

        self.ptr3 += 1
        self.ptr3_2 += 1

    def update_cpu(self):
        self.data_cpu = adb_fps_cpu_mem_flow.cpu_info_one(self.ser_num, self.app_name)
        print(self.data_cpu)
        print(self.data_cpu[self.ser_num][0])
        if not self.data_cpu:
            print("请打开gpu呈现模式中的adb或打开任意应用")
            self.data_cpu[self.ser_num][0] = 0
        print(self.data_cpu['xghmozaiwgcylr7p'][0])
        self.myGDate4[self.ptr4] = self.data_cpu[self.ser_num][0]
        if self.ptr4 + 1 >= self.myGDate4.shape[0]:
            tmp = self.myGDate4
            self.myGDate4 = np.empty(self.myGDate4.shape[0] * 2)
            self.myGDate4[:tmp.shape[0]] = tmp
        self.plot_data4.setData(self.myGDate4[:self.ptr4 + 1])
        self.ptr4 += 1

    # 每秒更新
    def timer_update_fps(self):
        self.timer = pg.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_fps)
        self.timer.start(1000)

    def timer_update_mem(self):
        self.timer2 = pg.QtCore.QTimer(self)
        self.timer2.timeout.connect(self.update_memory)
        self.timer2.start(1000)

    def timer_update_flow(self):
        self.timer3 = pg.QtCore.QTimer(self)
        self.timer3.timeout.connect(self.update_flow)
        self.timer3.start(1000)

    def timer_update_cpu(self):
        self.timer4 = pg.QtCore.QTimer(self)
        self.timer4.timeout.connect(self.update_cpu)
        self.timer4.start(1000)
        print("-------------------")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    # cgitb.enable()
    sys.exit(app.exec())
