import requests
import re
from  bs4 import BeautifulSoup


class LaGouWang():

    def __init__(self,s):
          self.s  = s

    def get_token(self):
        """
        function：
             获取拉勾网token和code两个参数
        param s:
            用来传  s = request.session()
        return:
            {"X_Anti_Forge_Token" : "X_Anti_Forge_Token","X_Anti_Forge_Code" : "X_Anti_Forge_Code"}
        """
        url = "https://passport.lagou.com/login/login.html"
        h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                }
        r = self.s.get(url,headers=h)
        t = r.content
        # print(t)
        soup = BeautifulSoup(t,"html.parser")
        all = soup.find_all("script")
        # print(all)
        a = all[1].string    #获取字符串用.string
        # print(a)
        res = {}
        try:
            X_Anti_Forge_Token = re.findall("Token = \'(.+?)\'",a)
            X_Anti_Forge_Code = re.findall("Code = \'(.+?)\'",a)
            res["X_Anti_Forge_Token"] = X_Anti_Forge_Token[0]
            res["X_Anti_Forge_Code"] = X_Anti_Forge_Code[0]
        except:
            print("获取token和code失败，给空字符串")
            res["X_Anti_Forge_Token"] ="X_Anti_Forge_Token[0] "
            res["X_Anti_Forge_Code"] =" X_Anti_Forge_Code[0]"
        return res

    def login(self,aaa,user,psw):
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
        self.s.headers.update(h2)
        # print(h2)
        r2 = s.post(url2,data=body)
        try:
            result = r2.json()
        except:
            result = r2.text
        # result = r1.json()
        return result

if __name__=="__main__":
    s = requests.session()
    t =  LaGouWang(s)               #定义对象
    res = t.get_token()           #对象实例化
    print(res)
    result = t.login(aaa=res,user=15600159023,psw="y123654")
    print("登录结果是：%s"%result)


