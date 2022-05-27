from random import randint

from PyQt6.QtGui import QIcon, QCloseEvent
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox
import sys
import cgitb


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("example")
        self.setWindowIcon(QIcon("asdf.png"))

        self.btn = QPushButton("enter", self)
        self.btn.setGeometry(100, 100, 100, 100)
        self.btn.setToolTip("<b>this</b>")
        self.btn.clicked.connect(self.showMessage)

        self.text = QLineEdit("input", self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(50, 50, 200, 30)

        self.show()

    def showMessage(self):
        # print(self.text.text())
        guessnum = int(self.text.text())
        print(self.num)
        print(guessnum)
        if guessnum > self.num:
            QMessageBox.about(self, "看结果", "大了")
            self.text.setFocus()
        elif guessnum < self.num:
            QMessageBox.about(self, "看结果", "小了")
            self.text.setFocus()
        else:
            QMessageBox.about(self, "看结果", "对了")
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, a0: QCloseEvent) -> None:
        # print(1)
        reply = QMessageBox.question(self, "确认", "确认退出吗")
        # print(reply)
        if reply == QMessageBox.StandardButton.Yes:
            a0.accept()
        else:
            a0.ignore()


if __name__ == "__main__":
    with open("test1_text.css") as f:
        css = f.read()

    app = QApplication(sys.argv)
    app.setStyleSheet(css)
    ex = Example()
    cgitb.enable()
    sys.exit(app.exec())
