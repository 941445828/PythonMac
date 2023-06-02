# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5040.pageobject.lmsCourse_page import LMSCoursePage
from version.v5040 import *
from version.v5040.testcase.test_Class import TestClassPageReload


class TestEditDiscuss:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_search_logo(self, web_driver):
        LMSCoursePage().click_search_logo(web_driver)

    def test_enter_search_content(self, web_driver):
        LMSCoursePage().enter_search_content(web_driver, 'discuss', 20)

    def test_click_discuss_item(self, web_driver):
        LMSCoursePage().click_activities_item(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "/discuss/detail?")

    def test_click_edit_enter(self, web_driver):
        LMSCoursePage().click_discuss_edit_enter(web_driver)

    def test_click_edit(self, web_driver):
        LMSCoursePage().click_edit_btn(web_driver)

    def test_switch_win_3(self, web_driver):
        get_new_page_special(web_driver, "discuss/edit")

    def test_click_edit_ensure(self, web_driver):
        LMSCoursePage().click_edit_ensure_web(web_driver)

    def test_switch_win_4(self, web_driver):
        get_new_page_special(web_driver, "/discuss/detail?")

    def test_edit_discuss_close_11(self, web_driver):
        LMSCoursePage().click_discuss_page_closed(web_driver)

    def test_switch_win_5(self, web_driver):
        get_new_page_special(web_driver, "r&searchKey=discuss")

    # def test_search_content_del(self, web_driver):
    #     """ 清除搜索内容 """
    #     LMSCoursePage().enter_search_content_del(web_driver)

    def test_page_reload(self, native_driver):
        """点击页面上的reload 重新加载"""
        TestClassPageReload().test_class_page_reload(native_driver)
