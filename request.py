__author__ = 'Wangxiaofeng'

import requests as req
import HTMLTestRunner
import random


test_url = "https://mail.126.com/js6/main.jsp"
p = {"sid": "EABFeLaaJgUOppxwikaaRNBTQSYKQGha", "df": "mail126_letter#module=welcome.WelcomeModule%7C%7B%7D"}
h = {"User-Agent": "Android/H60-L01/4.4.2/"}
c = {"JSESSIONID" : "01CAC794399A0586CFEB6F8264BFA8BF"}
response = req.get(test_url, headers=h, cookies=c, params=p)
print(response.status_code)

print(response.headers)
print(response.text)


# if __name__ == "__main__":
    # fr = open("res1.html", "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream= fr,title= "测试报告")

mobile = random.randint(13000000000, 13999999999)
print(mobile)