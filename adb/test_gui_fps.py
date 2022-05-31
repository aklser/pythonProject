import random

import numpy as np
import pyqtgraph as pg
import adb_cpu_fps_mem as adb_cfm


def update1():
    global ptr1
    for i in c:
        try:
            d[i][:-1] = d[i][1:]  # 将数组中的数据向左移动一个样本
            d[i][-1] = data_all[i][0]
            c[i].setData(d[i])
            c[i].setPos(ptr1+1, 0)
        except:
            print("请打开应用或对应用进行操作！")
    ptr1 += 1


def update2():
    global ptr2
    print(b)
    for i in a:
        try:
            b[i][ptr2] = data_all[i][0]
            print(b)
        except:
            print("请打开应用或对应用进行操作！")
        else:
            if ptr2 + 1 >= b[i].shape[0]:
                tmp = b[i]
                b[i] = np.empty(b[i].shape[0] * 2)
                b[i][:tmp.shape[0]] = tmp
            a[i].setData(b[i][:ptr2 + 1])
    ptr2 += 1


# 更新所有绘图
def update():
    global data_all
    data_all = adb_cfm.do_fps_line("com.tencent.tim")
    update1()
    update2()


if __name__ == '__main__':
    win = pg.GraphicsLayoutWidget(show=True)
    win.setWindowTitle('test_fps')

    p1 = win.addPlot()
    c = {}
    d = {}
    print(adb_cfm.devices_info)
    for i in adb_cfm.devices_info:
        d[i] = np.zeros(shape=10)
        c[i] = p1.plot(d[i], pen=(0, random.randint(175, 255), random.randint(175, 255)))
    ptr1 = 0

    win.nextRow()
    p2 = win.addPlot()
    a = {}
    b = {}
    for i in adb_cfm.devices_info:
        a[i] = p2.plot(pen=(0, random.randint(175, 255), random.randint(175, 255)))
        b[i] = np.empty(2)

    p2.showGrid(x=True, y=True)
    p2.setTitle("fps")
    p2.setLabel(axis="left", text="帧率")
    p2.setLabel(axis="bottom", text="time")
    p2.setDownsampling(mode='peak')
    p2.setClipToView(True)
    ptr2 = 0

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1000)
    pg.exec()
