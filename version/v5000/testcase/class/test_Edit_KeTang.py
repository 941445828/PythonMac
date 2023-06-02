# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from config import stability_conf
from version.v5000.pageobject.lmsCourse_page import LMSCoursePage
from version.v5000 import *
from version.v5000.testcase.test_Class import TestClassPageReload


class TestEditKeTang:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_search_logo(self, web_driver):
        LMSCoursePage().click_search_logo(web_driver)

    def test_enter_search_content(self, web_driver):
        LMSCoursePage().enter_search_content(web_driver, stability_conf.CLASSNAME, 20)

    # 11/15修改搜索bug后，交互变了，这个不要了; # 12.30又更改回来了
    def test_switch_win_11(self, web_driver):
        get_new_page_special(web_driver, "searchKey=" + stability_conf.CLASSNAME)

    def test_click_ketang_item(self, web_driver):
        LMSCoursePage().click_activities_item(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "processFlag")

    def test_click_edit_enter(self, web_driver):
        LMSCoursePage().click_ketang_edit_enter(web_driver)

    def test_click_edit(self, web_driver):
        LMSCoursePage().click_edit_btn(web_driver)

    def test_switch_win_33(self, web_driver):
        get_new_page_special(web_driver, "unitId")

    def test_edit_allow_check(self, web_driver):
        LMSCoursePage().click_edit_allow_check(web_driver)

    def test_click_edit_ensure(self, native_driver):
        LMSCoursePage().click_edit_ensure_native(native_driver)

    def test_switch_win_4(self, web_driver):
        get_new_page_special(web_driver, "processFlag")

    def test_edit_ketang_close_12(self, web_driver):
        LMSCoursePage().click_ketang_page_closed(web_driver)

    def test_switch_win_5(self, web_driver):
        get_new_page_special(web_driver, "&searchKey=" + stability_conf.CLASSNAME)

    def test_search_content_del(self, web_driver):
        """ 清除搜索内容 """
        LMSCoursePage().enter_search_content_del(web_driver)

    def test_page_reload(self, native_driver):
        """点击页面上的reload 重新加载"""
        TestClassPageReload().test_class_page_reload(native_driver)
