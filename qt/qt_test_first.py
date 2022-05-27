import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("name")
window.resize(1080, 600)
window.move(100, 100)

btn = QPushButton(window)
btn.setText("按钮")
btn.resize(200, 100)
btn.move(100, 100)
btn.setStyleSheet("background-color:green;font-size:16px;")

label = QLabel(window)
label.setText("标签")
label.setStyleSheet("background-color:green;font-size:16px;")

window.show()
label.show()
sys.exit(app.exec())
