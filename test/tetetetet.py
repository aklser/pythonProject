# a = "asdas,fasda,sfa:f fas"
# b = ""
# for i in a:
#     if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
#         b = b + i
# print(b)
# print(5//2)
# a = {"a": 12}
#
# if a.get("b"):
#     print(a)
# else:
#     print("ads")


# def g_up(func):
#     def m(*args, **kwargs):
#         a = func(*args, **kwargs)
#         a = a.capitalize()
#         return a
#
#     return m
#
#
# @g_up
# def gu(word="asd fa"):
#     return word.lower()
#
#
# print(gu("asdfa"))
# a={1:123}
# print(a.get(1))
# def ge_func():
#     yield 1
#     yield 2
#     yield 3
#
#
# # 第一种调用
# a = ge_func()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# # 第二种调用
# myge = ge_func()
# for item in myge:
#     print(item)
#
# # 第三种调用
# for item in ge_func():
#     print(item)
# import sys
# from PyQt6.QtWidgets import QWidget, QGridLayout, QLCDNumber, QApplication, QPushButton
# import cgitb
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.Init_UI()
#
#     def Init_UI(self):
#         self.setGeometry(300, 300, 400, 400)
#         self.setWindowTitle("学点编程吧计算器")
#         self.show()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
