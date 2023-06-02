# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5010.pageobject.lmsCourse_page import LMSCoursePage
from version.v5010 import *
from handler.yamlHandler import get_data


class TestCopyOtherClassActivities:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "&role=manager")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_copy_class_activity(self, web_driver):
        LMSCoursePage().click_copy(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "import")

    def test_copy_select_class(self, web_driver):
        case = get_data('baseConf.yaml')[0]
        copy_class = case['class_for_copy']
        LMSCoursePage().choose_class(web_driver, copy_class)

    def test_switch_win_3(self, web_driver):
        get_new_page_special(web_driver, "activity-select")

    def test_select_unit(self, web_driver):
        LMSCoursePage().choose_unit(web_driver)

    def test_copy_class_continue(self, web_driver):
        LMSCoursePage().click_Continue(web_driver)

    def test_switch_win_4(self, web_driver):
        get_new_page_special(web_driver, "activity-setting")

    def test_copy_class_insure(self, web_driver):
        LMSCoursePage().click_sure(web_driver)
