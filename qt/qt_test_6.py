import sys

from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal, QObject
import cgitb


class Signal(QObject):
    showmouse = pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("?")
        self.s = Signal()
        self.s.showmouse.connect(self.about)
        self.show()

    def about(self):
        QMessageBox.about(self, "?", "dianji")

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.s.showmouse.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    cgitb.enable()
    sys.exit(app.exec())
