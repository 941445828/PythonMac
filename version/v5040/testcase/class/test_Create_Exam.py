# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5040.pageobject.lmsCourse_page import LMSCoursePage
from version.v5040 import *


class TestCreateExam:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_exam(self, web_driver):
        """ 点击 新建里的 测验"""
        LMSCoursePage().click_exam(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "/ExamEditor")

    def test_exam_select_all(self, web_driver):
        """ 选题"""
        LMSCoursePage().click_select_item(web_driver)

    def test_paper_set(self, web_driver):
        """组卷设置"""
        LMSCoursePage().click_select_set(web_driver)

    def test_paper_title(self, web_driver):
        """输入 试卷 标题"""
        LMSCoursePage().enter_exam_title(web_driver)

    def test_paper_publish(self, web_driver):
        """ 发布 """
        LMSCoursePage().click_exam_publish(web_driver)
