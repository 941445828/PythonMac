# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5040.pageobject.lmsCourse_page import LMSCoursePage
from version.v5040 import *


class TestCreateHomework:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_hw(self, web_driver):
        """ 点击 新建里的 作业"""
        LMSCoursePage().click_homework(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "homework")

    def test_hw_input_name(self, web_driver):
        """ 作业，输入名称 """
        LMSCoursePage().enter_hw_name(web_driver)

    def test_hw_input_content(self, web_driver):
        """ 作业，输入内容 """
        LMSCoursePage().enter_hw_content(web_driver)

    def test_hw_publish(self, web_driver):
        """ 点击 发布"""
        LMSCoursePage().click_publish_btn(web_driver)
