# -*- coding: utf-8 -*-

"""
Module implementing ExchangeRate.
"""

import sys
import pandas
import pyqtgraph as pg
from PyQt5.QtGui import QPicture, QPainter
from PyQt5.QtCore import pyqtSlot, QRect, QPointF, QRectF
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_ui import Ui_MainWindow


class DrawChart():
    def __init__(self):
        self.data_list, self.t = self.getData()

    def pyqtgraphDrawChart(self):
        try:
            self.item = CandlestickItem(self.data_list)
            self.xdict = {0: self.data_list[0][1],
                          int((self.t + 1) / 2) - 1: self.data_list[int((self.t + 1) / 2) - 1][1],
                          self.t - 1: self.data_list[-1][1]}
            self.stringaxis = pg.AxisItem(orientation='bottom')
            self.stringaxis.setTicks([self.xdict.items()])
            self.plt = pg.PlotWidget(axisItems={'bottom': self.stringaxis}, enableMenu=False)
            self.plt.addItem(self.item)
            return self.plt
        except:
            return pg.PlotWidget()

    def getData(self):
        self.exr_data = pandas.read_csv("rmb.csv").sort_index(ascending=False)
        data_list = []
        t = 0
        for index, row in self.exr_data.iterrows():
            date, close, open, high, low, price_change = row
            datas = (t, date, close, open, high, low, price_change)
            data_list.append(datas)
            t = t + 1
        return data_list, t


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()

    def generatePicture(self):
        self.picture = QPicture()
        p = QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, date, close, open, high, low, price_change) in self.data:
            if open > close:
                p.setPen(pg.mkPen('g'))
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setPen(pg.mkPen('r'))
                p.setBrush(pg.mkBrush('r'))
            if low != high:
                p.drawLine(QPointF(t, low), QPointF(t, high))
            p.drawRect(QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QRectF(self.picture.boundingRect())


class ExchangeRate(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ExchangeRate, self).__init__(parent)
        self.setupUi(self)
        self.InitUi()

    def InitUi(self):
        self.splitter.setStretchFactor(0, 4)
        self.splitter.setStretchFactor(1, 6)
        pg.setConfigOption('background', '#f0f0f0')
        self.drawChart = DrawChart()
        self.exrwidget = self.drawChart.pyqtgraphDrawChart()
        self.verticalLayout.addWidget(self.exrwidget)
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.exrwidget.addItem(self.vLine, ignoreBounds=True)
        self.exrwidget.addItem(self.hLine, ignoreBounds=True)
        self.exrwidget.scene().sigMouseMoved.connect(self.mouseMoved)

    def mouseMoved(self, pos):
        vb = self.exrwidget.plotItem.vb
        if self.exrwidget.sceneBoundingRect().contains(pos):
            mousePoint = vb.mapSceneToView(pos)
            index = int(mousePoint.x() + 1 / 3.)
            if index >= 0 and index < len(self.drawChart.data_list):
                date, close, open, high, low, price_change = self.drawChart.data_list[index][1::]
                self.label_date_c.setText(date)
                self.label_close_c.setText(str(close))
                self.label_open_c.setText(str(open))
                self.label_high_c.setText(str(high))
                self.label_low_c.setText(str(low))
                self.label_change_c.setText(price_change)
                if price_change[0] == "-":
                    self.label_change_c.setStyleSheet("color:green")
                elif price_change == "0.00%":
                    self.label_change_c.setStyleSheet("color:black")
                else:
                    self.label_change_c.setStyleSheet("color:red")
                self.vLine.setPos(mousePoint.x())
                self.hLine.setPos(mousePoint.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exrate = ExchangeRate()
    exrate.show()
    sys.exit(app.exec_())
