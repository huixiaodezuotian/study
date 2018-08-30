# coding:utf-8
from bs4 import BeautifulSoup
import requests


# 获取Html信息
url = "https://www.qiushibaike.com/"
r = requests.get(url)
t = r.text
print(t)

# HTML对象
soup = BeautifulSoup(t,"html.parser")

# 打印层级关系
# print(soup.prettify())

# 查找所有class
all = soup.find_all(class_ = "content")             #find_all查找的是一个list对象
# print(all)
for i in all:
    # print(i)
    # get_text()获取tag标签下所有的文本
    print(i.span.get_text().replace("\n"," "))          #replace替换字符串里面的特殊字符