import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen, QMouseEvent, QPaintEvent
import cgitb


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setMouseTracking(True)

    def initUi(self):
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle("qwer")
        self.label = QLabel(self)
        self.label.resize(500, 20)
        self.show()
        self.pos = None


    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        print(a0.pos())
        distance_from_center = round(((a0.pos().y()) ** 2 + (a0.pos().x()) ** 2) ** 0.5)

        self.label.setText(str(a0.pos()) + "," + str(distance_from_center))
        self.pos = a0.pos()
        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        if self.pos:
            q = QPainter(self)

            q.drawLine(0, 0, self.pos.x(), self.pos.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example1()
    cgitb.enable()
    sys.exit(app.exec())
