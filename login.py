__author__ = 'Wangxiaofeng'
#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import unittest
from urllib import parse
import HTMLTestRunner
from datetime import datetime
import random
from logger import Log

class LoginRegisterTest(unittest.TestCase):
    # 测试登陆注册接口

    def setUp(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url = 'http://39.105.191.175:8080/twweb'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}

    def test_login_success(self):
        """
        登陆成功
        :return:
        """
        logging.debug('run case,test case name:test_login_success')
        url_login = self.url + '/LoginController_4M/login.action?'
        user_info1 = self.user_info.copy()
        user_info1['logintype'] = '2'
        r = requests.post(url_login, data=user_info1)
        self.assertIn('登录成功', parse.unquote(parse.unquote(r.text)))

    def test_login_fail1(self):
        """
        密码错误
        :return:
        """
        logging.debug('run case,test case name:test_login_fail1')
        url_login = self.url + '/LoginController_4M/login.action?'
        user_info2 = self.user_info.copy()
        user_info2['logintype'] = '2'
        user_info2['password'] = '0'
        r = requests.post(url_login, data=user_info2)
        self.assertIn('用户名或密码错误', parse.unquote(parse.unquote(r.text)))

    def test_login_fail2(self):
        """
        用户名错误
        :return:
        """
        logging.debug('run case,test case name:test_login_fail2')
        url_login = self.url + '/LoginController_4M/login.action?'
        user_info3 = self.user_info.copy()
        user_info3['logintype'] = '2'
        user_info3['mobile'] = '123'
        r = requests.post(url_login, data=user_info3)
        self.assertIn('用户名或密码错误', parse.unquote(parse.unquote(r.text)))

    def verification_code(self):
        """
        注册验证码
        :return:(mobile, text.split(',')[0].split(':')[3][8:14])
        """
        url_ver = self.url + '/UserController_4M/registeMessage.action?'
        mobile = random.randint(14611111000, 14611119999)
        r = requests.post(url_ver, data={'mobile': mobile})
        text = parse.unquote(parse.unquote(r.text))
        self.assertIn('天娃新时代', text)
        return mobile, text.split(',')[0].split(':')[3][8:14]

    def test_register1(self):
        """
        推荐人非创客时注册成功
        :return:
        """
        logging.debug('run case,test case name:test_register1')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': ver_code[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': '14611110001',
            'checkCode': ver_code[1],
            'fan_shop_mobile': None
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('注册成功', parse.unquote(parse.unquote(r.text)))

    def test_register2(self):
        """
        推荐人为创客时注册成功
        :return:
        """
        logging.debug('run case,test case name:test_register2')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': ver_code[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': '14611110000',
            'checkCode': ver_code[1],
            'fan_shop_mobile': '14611110001'
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('注册成功', parse.unquote(parse.unquote(r.text)))

    def test_register_fail1(self):
        """
        推荐人为空时注册失败
        :return:
        """
        logging.debug('run case,test case name:test_register_fail1')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': ver_code[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': None,
            'checkCode': ver_code[1],
            'fan_shop_mobile': None
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('注册失败!', parse.unquote(parse.unquote(r.text)))

    def test_register_fail2(self):
        """
        验证码错误时注册失败
        :return:
        """
        logging.debug('run case,test case name:test_register_fail2')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': ver_code[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': None,
            'checkCode': '12345',
            'fan_shop_mobile': None
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('注册失败!', parse.unquote(parse.unquote(r.text)))

    def test_register_fail3(self):
        """
        不输入手机号时注册失败
        :return:
        """
        logging.debug('run case,test case name:test_register_fail3')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': None,
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': None,
            'checkCode': ver_code[1],
            'fan_shop_mobile': None
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('注册失败!', parse.unquote(parse.unquote(r.text)))

    def test_register_fail4(self):
        """
        推荐人为创客时不输入绑粉商家编号时注册失败
        :return:
        """
        logging.debug('run case,test case name:test_register_fail4')
        url_register = self.url + '/UserController_4M/insertUser.action? '
        ver_code = self.verification_code()
        form_register = {
            'mobile': ver_code[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': '14611110000',
            'checkCode': ver_code[1],
            'fan_shop_mobile': None
        }
        r = requests.post(url_register, data=form_register)
        self.assertIn('请重新输入绑粉商家编号', parse.unquote(parse.unquote(r.text)))


def suite():
    """
    测试套件
    :return: loginTestCases
    """
    login_test_cases = unittest.makeSuite(LoginRegisterTest, 'test')
    return login_test_cases


if __name__ == "__main__":
    logging = Log().get_instance('tw')
    with open("F:/ScriptReport/report_" + datetime.now().strftime('%Y%m%d-%H-%M') + ".html", 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='测试报告', description='详情')
        runner.run(suite())
