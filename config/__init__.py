# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import os
import datetime
import time
import pytest
import pyautogui
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass


"""项目 根目录地址"""
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(PROJECT_DIR)


"""启动的APP"""
APP = "ClassIn"


"""webview driver"""
WEBVIEW_DRIVER_URL = PROJECT_DIR + '/tools/chromedriver'
# print(WEBVIEW_DRIVER_URL)
WEB_DRIVER_103 = PROJECT_DIR + '/tools/chromedriver-mac-intel-103'

"""web inspector url"""
INSPECT_URL = "127.0.0.1:7777"


""" 获取系统用户名 """
SYS_USER = getpass.getuser()
# print(SYS_USER)
