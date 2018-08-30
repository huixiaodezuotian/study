import requests
import re
from  bs4 import BeautifulSoup



def get_token(s):
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
    r = s.get(url,headers=h)
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
        res["X_Anti_Forge_Token"] =" "
        res["X_Anti_Forge_Code"] =" "
    return res



if __name__=="__main__":
    s = requests.session()
    res = get_token(s)
    print(res)

