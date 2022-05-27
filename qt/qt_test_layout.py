import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("?")

        btn = QPushButton("?", self)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addStretch(1)

        vbox = QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
