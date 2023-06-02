# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5040.pageobject.lmsCourse_page import LMSCoursePage
from version.v5040 import *


class TestCreateDiscuss:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "&role=manager")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_discuss(self, web_driver):
        """ 点击 新建里的 讨论"""
        LMSCoursePage().click_discuss(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "discuss")

    def test_discuss_input_title(self, web_driver):
        """ 填写 讨论 标题 """
        LMSCoursePage().enter_dis_title(web_driver)

    def test_discuss_input_content(self, web_driver):
        """ 填写 讨论 内容"""
        LMSCoursePage().enter_dis_content(web_driver)

    def test_discuss_publish(self, web_driver):
        """ 发布"""
        LMSCoursePage().click_publish_btn(web_driver)
