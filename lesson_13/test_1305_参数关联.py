# coding:utf-8
import  requests
import re
from  bs4 import BeautifulSoup


def login(s,aaa,user,psw):
    url2 = "https://passport.lagou.com/login/login.json"
    h2 = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
        "X-Anit-Forge-Token":aaa["X_Anti_Forge_Token"],
        "X-Anit-Forge-Code":aaa["X_Anti_Forge_Code"],
        "Referer":"https://passport.lagou.com/login/login.html"
        }
    body = {
            "isValidate":"true",
            "username":user,
            "password":psw,
            "request_form_verifyCode":" ",
            "submit":" "
                }
    # s = requests.session()
    s.headers.update(h2)
    # print(h2)
    r2 = s.post(url2,data=body)
    try:
        result = r2.json()
    except:
        result = r2.text
    # result = r1.json()
    return result

if __name__=="__main__":
    from lesson_13.lgw import get_token
    s = requests.session()
    r = get_token(s)
    print(r)
    result = login(s,aaa=r,user="15600159023",psw="y123456")
    print("登录结果是：%s"%result)





