import cgitb

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QProgressDialog, QMessageBox
import sys
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("?")

        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 20)

        self.bt = QPushButton("开始", self)
        self.bt.move(20, 50)

        self.editnum = QLineEdit("1000", self)
        self.editnum.move(100, 20)

        self.bt.clicked.connect(self.showDialog)
        self.show()

    def showDialog(self):
        num = int(self.editnum.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在执行程序...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(4)
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    cgitb.enable()
    sys.exit(app.exec())
