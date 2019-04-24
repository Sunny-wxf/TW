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


class HomePage(unittest.TestCase):
    # 首页所有接口

    __logging = Log().get_instance('tw_homepage')

    def setUp(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url_twweb = 'http://39.105.191.175:8080/twweb'
        self.url_system = 'http://39.105.191.175:8080/tw_system'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}

    def test_version_update(self):
        """
        更新接口
        :return:
        """
        self.__logging.debug('run case,test case name:test_version_update')
        url = self.url_system + '/AppVersionUpdate_Controller_4W/appVersionUpdateInfo.action?'
        form = dict(os='android', version_code='1.3.3', manufacturer='Xiaomi', model='MI5X', sdk_version='7.1.2')
        r = requests.post(url=url, data=form)
        self.assertEqual('200', str(r.status_code))



class Suite(object):

    def home_suite(self):
        """
        测试套件
        :return: loginTestCases
        """
        home_test_cases = unittest.makeSuite(HomePage, 'test')
        return home_test_cases

    def test_report(self):
        with open("F:/ScriptReport/report_" + datetime.now().strftime('%Y%m%d-%H-%M') + ".html", 'wb') as report:
            runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='测试报告', description='详情')
            runner.run(self.home_suite())


if __name__ == '__main__':
    suite = Suite()
    suite.test_report()





