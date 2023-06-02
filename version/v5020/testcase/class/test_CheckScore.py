# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5010 import *
from version.v5010.pageobject.lmsCourse_page import LMSCoursePage


class TestCheckScore:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "score")

    def test_change_to_study_activity(self, web_driver):
        """切换到 学习活动 tab"""
        LMSCoursePage().click_study_activity(web_driver)

    def test_click_student(self, web_driver):
        """ 点击 学生列表 下的 第一个人"""
        LMSCoursePage().click_student(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "&role=manager&isStudentView=")

    def test_view_score_close_05(self, web_driver):
        """关闭 学生 成绩页面"""
        LMSCoursePage().click_score_page_closed(web_driver)


