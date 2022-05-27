import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu, QMessageBox
from PyQt6.QtGui import QIcon, QAction, QContextMenuEvent


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUi()

    def InitUi(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("?")

        self.statusBar().showMessage("准备就绪")

        exitact = QAction(QIcon("asdf.png"), "退出(&E)", self)
        exitact.setStatusTip("退出")
        exitact.triggered.connect(QApplication.quit)

        saveMenu = QMenu("保存方式", self)

        saveAct = QAction(QIcon("asdf.png"), "保存", self)
        saveAct.setStatusTip("保存文件")

        saveasAct = QAction(QIcon("asdf.png"), "另存为", self)
        saveasAct.setStatusTip("文件另存为")

        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon("asdf.png"), "新建", self)
        newAct.setStatusTip("新建文件")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件(&A)")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitact)

        toolbar = self.addToolBar("工具栏")
        toolbar.addAction(newAct)
        toolbar.addAction(exitact)

        self.show()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        cmenu = QMenu(self)
        newAct = cmenu.addAction("新建")
        saveAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec(self.mapToGlobal(event.pos()))
        if action == quitAct:
            QApplication.quit()
        elif action == saveAct:
            QMessageBox.about(self, "?", "保存成功！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
