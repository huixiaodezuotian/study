import requests
from bs4 import BeautifulSoup

url = "http://699pic.com/sousuo-218808-13-1-0-0-0.html"
r = requests.get(url)
t = r.content
# print(t)
soup = BeautifulSoup(t,"html.parser")
all = soup.find_all(class_="lazy")
# print(all)
for i in all:
    # print(i)
    try:                                    #用try except捕获异常处理
        jpg_url =i["data-original"]         #通过tag对象取属性
        print(jpg_url)
        jpg_title = i["title"]
        print(jpg_title)
        r2 = requests.get(jpg_url)
        with open(jpg_title+".jpg","wb") as fp:
            fp.write(r2.content)            #保存，打开
    except:
        pass


