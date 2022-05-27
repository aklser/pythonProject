import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("学")

        self.lab = QLabel("方向", self)
        self.lab.setGeometry(180, 180, 40, 40)
        self.show()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Up:
            self.lab.setText("up")
        elif a0.key() == Qt.Key.Key_Down:
            self.lab.setText("down")
        elif a0.key() == Qt.Key.Key_Left:
            self.lab.setText("left")
        elif a0.key() == Qt.Key.Key_Right:
            self.lab.setText("right")
        else:
            self.lab.setText("qwq")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
