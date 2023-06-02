# coding = utf-8
"""
@Author: sujie
@Create on: 2021
@Modify on：
@File: 在线教室相关
"""
from version.v5000 import *
from config import perf_conf
from version.v5000.pageobject.onlineclassroom_page import Tool_YunPan, OpenFile, Close_File
from handler.yamlHandler import get_data
from version.v5000 import *


class TestOnLineOpenFiles(object):
    def test_click_yunpan(self, native_driver):
        Tool_YunPan().click_tool_yunpan(native_driver)

    def test_click_wendang(self, web_driver):
        time.sleep(2)
        get_new_page_special(web_driver, "inspector")
        OpenFile().click_wendang(web_driver)

    def test_open_file(self, web_driver):
        case = get_data('baseConf.yaml')[0]
        # 点击文件夹
        OpenFile().click_folder(web_driver, case['target_yunpan_folder'])
        # 点击要打开的课件

        files_list = perf_conf.open_files_setting
        print('open:')
        for i in range(len(files_list)):
            print(files_list[i])
            OpenFile().click_file(web_driver, files_list[i])
            time.sleep(60)
        time.sleep(90)


class TestOnlineCloseFiles:
    def test_close_files(self, native_driver):
        Close_File().get_files(native_driver)
