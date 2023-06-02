# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LMSCoursePage
from version.v5000 import *


class TestCreateUnitTopic:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_unit_topic(self, web_driver):
        LMSCoursePage().click_unit(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "unit")

    def test_unit_topic_title(self, web_driver):
        LMSCoursePage().enter_unit_title(web_driver)

    def test_unit_topic_content(self, web_driver):
        LMSCoursePage().enter_unit_content(web_driver)

    def test_unit_topic_publish(self, web_driver):
        LMSCoursePage().click_publish_btn(web_driver)
