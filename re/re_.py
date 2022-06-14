import re

#
# s = "100 north road aroad road"
#
# print(s.replace("road", "ro."))
# print(re.sub(r"\broad\b", "ro.", s))
#
# print("*************")
# pattern = "^M?M?M?$"
# print(re.search(pattern, "MMM"))

# content = '''
# Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
# 测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
# Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
# 测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
# Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
# python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
# '''
# # for one in re.findall(r"([.\d]+)万/每{0,1}月", content):
# #     print(one)
#
# for i in re.findall("([\d]+)-", content):
#     print(i)

# source = '<html><head><title>Title</title>'
#
# # 注意多出的问号
# p = re.compile(r'<.*?>')
# print(p.findall(source))
#
# print(re.findall(r"<.*?>", source))
names = '''

下面是这学期要学习的课程：

<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律

<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式

<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''


# 替换函数，参数是 Match对象
def subFunc(match):
    # Match对象 的 group(0) 返回的是整个匹配上的字符串，
    src = match.group(0)

    # Match对象 的 group(1) 返回的是第一个group分组的内容
    number = int(match.group(1)) + 6
    dest = f'/av{number}/'

    print(f'{src} 替换为 {dest}')

    # 返回值就是最终替换的字符串
    return dest


newStr = re.sub(r'/av(\d+?)/', subFunc, names)
print(newStr)