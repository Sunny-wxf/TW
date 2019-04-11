__author__ = 'Wangxiaofeng'
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import unittest
from urllib import parse
import HTMLTestRunner
from datetime import datetime,date
import random

global url
url = 'http://39.105.191.175:8080/twweb'


class LoginRegisterTest(unittest.TestCase):
    # 测试登陆注册接口
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
        """
        密码错误
        :return:
        """
        url_login = url + '/LoginController_4M/login.action?'
        form_login2 = form.copy()
        form_login2['logintype'] = '2'
        form_login2['password'] = '0'
        r = requests.post(url_login, data=form_login2)
        self.assertIn('用户名或密码错误', parse.unquote(parse.unquote(r.text)))

    def testlogin_fail2(self):
        """
        用户名错误
        :return:
        """
        url_login = url + '/LoginController_4M/login.action?'
        form_login2 = form.copy()
        form_login2['logintype'] = '2'
        form_login2['mobile'] = '123'
        r = requests.post(url_login, data=form_login2)
        self.assertIn('用户名或密码错误', parse.unquote(parse.unquote(r.text)))

    def verificationcode(self):
        """
        注册验证码
        :return:(mobile, text.split(',')[0].split(':')[3][8:14])
        """
        url_ver = url + '/UserController_4M/registeMessage.action?'
        mobile = random.randint(14611111000, 14611119999)
        r = requests.post(url_ver, data={'mobile': mobile})
        text = parse.unquote(parse.unquote(r.text))
        self.assertIn('天娃新时代', text)
        return (mobile, text.split(',')[0].split(':')[3][8:14])


    def testregister(self):
        """
        推荐人非创客时注册成功
        :return:
        """
        url_rehister = url + '/UserController_4M/insertUser.action? '
        a= self.verificationcode()
        form_register = {
            'mobile': a[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': '14611110001',
            'checkCode': a[1],
            'fan_shop_mobile': None
        }
        r = requests.post(url_rehister, data=form_register)
        self.assertIn('注册成功', parse.unquote(parse.unquote(r.text)))

def suite():
    """
    测试套件
    :return: loginTestCases
    """
    loginTestCases = unittest.makeSuite(LoginRegisterTest, 'test')
    return loginTestCases


if __name__ == "__main__":
        with open("F:/ScriptReport/report_" + datetime.now().strftime('%Y%m%d-%H-%M') +".html", 'wb') as report:
            runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='测试报告', description='详情')
            runner.run(suite())




