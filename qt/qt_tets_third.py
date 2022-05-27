import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLCDNumber, QDial, QApplication, QSlider


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        slider = QSlider(self)

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("title")

        lcd.setGeometry(100, 100, 200, 100)
        dial.setGeometry(150, 250, 100, 100)
        dial.valueChanged.connect(lcd.display)
        slider.setGeometry(150, 350, 50, 50)
        slider.valueChanged.connect(lcd.display)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
