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
# def fun():
#     temp=[lambda x:x*i for i in range(4)]
#     return temp
# for every in fun():
#     print(every)
#     print(every(2))
def ge_func():
    yield 1
    yield 2
    yield 3


# # 第一种调用
# print(ge_func().__next__())
# print(ge_func().__next__())
# print(ge_func().__next__())
#
# # 第二种调用
# myge = ge_func()
# for item in myge:
#     print(item)
#
# # 第三种调用
# for item in ge_func():
#     print(item)

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         a = n
#         b = 1
#         i = 0
#         while a >= 0:
#             a = a - b
#             b = b + 1
#             i = i + 1
#             print(i)
#         return i - 1
# 
# 
# print(Solution().arrangeCoins(3))
# from collections import Counter
#
# str = "hellopython"
# ct = Counter()
# print(isinstance(ct, dict))  # True
#
# for item in str:
#     ct[item] = ct[item] + 1  # 对于 ct[item]，如果 item 不存在，默认为 0
#
# print(ct)
# from collections import Iterator
#
# def mycount(bgdata=0):  # 默认从 0 开始生成无数整数的生成器
#     # bgdata = bgdata
#     while True:
#         yield bgdata
#         bgdata += 1
#
# values = mycount(1)
# print(isinstance(values, Iterator))  # True（生成器是迭代器）
# for value in values:
#     print(value)
# import itertools
#
# values = itertools.cycle(u"老鸟python")  # 参数可以是任何 Python 内置容器以及自定义容器
# for value in values:
#     print(value)
# import base64

# mydata = b"\x80"  # \x80 换成十进制为 128，超越了 ascii 范围，为不可见字节
# datab64 = base64.b64encode(mydata)  # 编码为 base64 的可见字节
# print(datab64)
#
# mydata = base64.b64decode(datab64)
# print(mydata)  # 解码为不可见字节 \x80
#
# dataone = "p".encode("utf8")    # 可见字节
# datatwo = "鸟".encode("utf8")   # 不可见字节
#
# print(dataone)
# print(base64.b64encode(dataone))  # 编码可见字节为可见字节
# print(base64.b64encode(datatwo))  # 编码不可见字节为可见字节
#
# from html.parser import HTMLParser
#
# class MyHtmlParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("<%s>" % tag)
#
#     def handle_endtag(self, tag):
#         print("</%s>" % tag)
#
#     def handle_starendtag(self, tag, attrs):
#         print("<%s>" % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print("<!-- -->")
#
#     def handle_entityref(self, name):
#         print("&%s;" % name)
#
#     def handle_charref(self, name):
#         print("&#%s" % name)
#
# parser = MyHtmlParser()
# html = "<html><head></head><body><p>老鸟python</p></body>"
# parser.feed(html)


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 生成随机大写字母，ascii为 [65, 90]，
def rndChar():
    return chr(random.randint(65, 90))

# 生成填充颜色，返回 RGB 值，每个颜色值在(128, 255)之间
def rndColor():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

# 生成字体颜色，返回 RGB 值，每个颜色值在(0, 127)之间，在此我只是为了不和背景颜色重叠，大家可以自行设置。
def rndColor2():
    return (random.randint(0, 127), random.randint(0, 127), random.randint(0, 127))

# 图片大小（存放 5 个随机字母），宽度为：400，高度为：80
width = 80 * 5
height = 80

# 黑色背景，RGB值为：(0, 0, 0)
image = Image.new('RGB', (width, height), (0, 0, 0))

# 创建 Font 对象，设定字体大小为 36
font = ImageFont.truetype('C:/Windows/Fonts/verdana.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(5):
    draw.text((80 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 让验证码图片模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')