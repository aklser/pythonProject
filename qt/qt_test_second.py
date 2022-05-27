import sys

from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(200, 200)
#     w.move(100, 100)
#     w.setWindowTitle("demo1")
#     w.show()
#     sys.exit(app.exec())
#
class Ico(QWidget):
    def __init__(self):
        super(Ico, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle("demo2")
        self.setWindowIcon(QIcon("asdf.png"))

        qbtn = QPushButton("exit", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(50, 50)
        qbtn.move(50, 50)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec())
