import cgitb
import sys
import time

from PyQt6.QtCore import QThread, QMutex, pyqtSignal
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

qmut1 = QMutex()
qmut2 = QMutex()


class myTread(QThread):
    def __init__(self, l, qm):
        super(myTread, self).__init__()
        self.li = l
        self.qm = qm

    def run(self) -> None:
        self.qm.lock()
        for i in self.li:
            print(i)
            time.sleep(2)
        self.qm.unlock()


class myTread_s(QThread):
    sig = pyqtSignal()

    def __init__(self, l):
        super(myTread_s, self).__init__()
        self.li = l
        # self.qm = qm

    def run(self) -> None:
        # self.qm.lock()
        for i in self.li:
            print(i)
            time.sleep(2)
        # self.qm.unlock()
        self.sig.emit()


class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 500, 500)
        self.bt1 = QPushButton("1", self)
        self.bt2 = QPushButton("2", self)

        self.bt1.move(100, 100)
        self.bt2.move(100, 200)

        self.bt1.clicked.connect(self.click1)
        self.bt2.clicked.connect(self.click2)

        self.show()

    def click1(self):
        self.thread1 = myTread([1, 2, 3, 4], qmut1)
        self.thread1.start()

    def click2(self):
        self.bt2.setEnabled(False)
        self.thread2 = myTread_s(["q", "w", "e"])
        self.thread2.start()
        self.thread2.sig.connect(self.set_btn)

    def set_btn(self):
        self.bt2.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MyWin()
    cgitb.enable()
    sys.exit(app.exec())
