# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from config import stability_conf
from version.v5020.pageobject.lmsCourse_page import LMSCoursePage
from version.v5020 import *


class TestCreateLuboke:
    def test_switch_win_1(self, web_driver):
        """ 切换H5 页面"""
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_luboke(self, web_driver):
        """ 点击 新建里的  录播课"""
        LMSCoursePage().click_luboke(web_driver)

    def test_switch_win_2(self, web_driver):
        """切换，H5页面"""
        get_new_page_special(web_driver, "unitName")

    def test_luboke_input_name(self, web_driver):
        """ 录播课，输入名称 """
        LMSCoursePage().enter_luboke_name(web_driver)

    def test_luboke_click_yunpan(self, web_driver):
        """选择云盘"""
        LMSCoursePage().click_yunpan(web_driver)

    def test_switch_win_3(self, web_driver):
        get_new_page_special(web_driver, "cloud")

    def test_luboke_choose_folder(self, web_driver):
        """选择云盘 文件夹"""
        LMSCoursePage().choose_folder(web_driver, stability_conf.YUNPANFLODER)

    def test_luboke_choose_file(self, web_driver):
        """选择云盘 文件"""
        LMSCoursePage().choose_file(web_driver)

    def test_luboke_click_ensure(self, web_driver):
        """ 点击 【 确定】"""
        LMSCoursePage().click_btn_ensure(web_driver)

    def test_switch_win_4(self, web_driver):
        """ 切换 h5"""
        get_new_page_special(web_driver, "unitName=")

    def test_luboke_pulish(self, web_driver):
        """ 点击 发布"""
        LMSCoursePage().click_publish_btn(web_driver)
