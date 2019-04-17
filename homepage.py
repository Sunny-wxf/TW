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

class HomePage():
    # 首页所有接口

    def setUp(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url_twweb = 'http://39.105.191.175:8080/twweb'
        self.url_system = 'http://39.105.191.175:8080/tw_system'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}

    def version_update(self):
        """
        更新接口无更新
        :return:
        """
        url = self.url_system + '/AppVersionUpdate_Controller_4W/appVersionUpdateInfo.action?'