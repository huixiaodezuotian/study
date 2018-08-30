# coding:utf-8
from bs4 import BeautifulSoup

# 读取yoyo.html
wangye = open("yoyo.html")
# print(wangye.read())

# BeautifulSoup  就是整个html对象
"""
构建一个 BeautifulSoup 对象需要两个参数，
第一个参数是将要解析的 HTML 文本字符串，
第二个参数告诉 BeautifulSoup 使用哪个解析器来解析 HTML
"""
soup = BeautifulSoup(wangye,"html.parser")
# 查找a标签
a = soup.a
print(a)

# 属性转字典
att = a.attrs
print(att)

# 获取文本属性
print(a.string)

# 获取href属性
print(att["href"])

# 获取class属性，由于class属性一般可以为多个，中间空格隔开，所以class属性获取的是一个list类型：[u'sister']
print(att["class"])

# 查找所有 a 标签
all = soup.find_all("a")    #1.find_all查找的是一个list对象
print(all)
print(all[2])           #获取列表中的第2个元素
for i in all:
    print(i)


# print(type(soup))
# print(soup.prettify())
#
# # tag 标签对象，如：<p class="title"><b>yoyoketang</b></p>
"""
BeatifulSoup 将 HTML 抽象成为 4 类主要的数据类型，分别是Tag , NavigableString , BeautifulSoup，Comment 。
每个标签节点就是一个Tag对象，
NavigableString 对象一般是包裹在Tag对象中的字符串，
BeautifulSoup 对象代表整个 HTML 文档
"""
# tag = soup.title
# print(type(tag))
# print(tag)
#
# # 多个标签名字相同，获取第一个标签名
# tag1 = soup.p
# print(tag1)
# print(tag1.b)
# # NavigableString 字符对象string，如：yoyoketang
# tag2 = soup.p
# print(type(tag.string))
# print(tag.string)
#
# # Comment    注释对象，如：!--for HTML5 --，它其实就是一个特殊NavigableString
# comment = soup.b.string
# print(type(comment))
# print(comment)


