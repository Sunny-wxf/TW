__author__ = 'Wangxiaofeng'

#!/usr/bin/python
# -*- coding:utf-

import requests
import unittest
from urllib import parse

global url
url = 'http://39.105.191.175:8080/twweb'


# 测试登陆接口
class LoginTest(unittest.TestCase):
    global form
    form = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}

    def testlogin_success(self):
        '''
        登陆成功
        :return:
        '''
        url_login = url + '/LoginController_4M/login.action?'
        form_login1 = form.copy()
        form_login1['logintype'] = '2'
        r = requests.post(url_login, data=form_login1)
        self.assertIn('登录成功', parse.unquote(parse.unquote(r.text)))

    def testlogin_fail1(self):
        '''
        密码错误
        :return:
        '''
        url_login = url + '/LoginController_4M/login.action?'
        form_login2 = form.copy()
        form_login2['logintype'] = '2'
        form_login2['password'] = '0'
        r = requests.post(url_login, data=form_login2)
        self.assertIn('用户名或密码错误', parse.unquote(parse.unquote(r.text)))


def suite():
    loginTestCases = unittest.makeSuite(LoginTest, 'test')
    return loginTestCases


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())


