import sys
from PyQt6.QtWidgets import QWidget, QApplication
from pyqtgraph import PlotWidget


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 700, 500)
        self.plw = PlotWidget(self)
        self.plw.setGeometry(10, 10, 300, 300)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
