# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LMSCoursePage
from handler.getWinHandler import get_win
from version.v5000 import *


class TestCreateNoLuKeKeTang:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)
        time.sleep(2)

    def test_new_create_ketang(self, web_driver):
        """ 点击 新建 --课堂"""
        LMSCoursePage().click_ketang(web_driver)

    def test_click_online_mode(self, native_driver):
        LMSCoursePage().click_online_mode(native_driver)

    def test_new_create_ketang_publish(self, native_driver):
        """发布"""
        get_win(native_driver, -2)
        LMSCoursePage().click_ketang_publish(native_driver)


class TestCreateLuKeKeTang:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)
        time.sleep(2)

    def test_new_create_ketang(self, web_driver):
        """ 点击 新建 --课堂"""
        LMSCoursePage().click_ketang(web_driver)

    def test_click_online_mode(self, native_driver):
        LMSCoursePage().click_online_mode(native_driver)

    def test_get_page_down(self, native_driver):
        LMSCoursePage().get_page_down(native_driver)

    def test_click_luke_room(self, native_driver):
        LMSCoursePage().click_luke_room(native_driver)

    def test_click_luke_onsite(self, native_driver):
        LMSCoursePage().click_luke_onsite(native_driver)

    def test_click_page_zhibo(self, native_driver):
        LMSCoursePage().click_page_zhibo(native_driver)

    def test_click_page_huifang(self, native_driver):
        LMSCoursePage().click_page_huifang(native_driver)

    def test_new_create_ketang_publish(self, native_driver):
        """发布"""
        get_win(native_driver, -2)
        LMSCoursePage().click_ketang_publish(native_driver)


class TestCreateKeTang:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "course/list")

    def test_moveto_last_unit(self, web_driver):
        """ 焦点定位至单元列表的最后一个，让’+‘号显示出来"""
        LMSCoursePage().move_to_unit(web_driver)

    def test_click_add_btn(self, web_driver):
        """ 点击'+'号 """
        LMSCoursePage().click_add_btn(web_driver)
        time.sleep(2)

    def test_click_ketang(self, web_driver):
        """ 点击-课堂， 添加课堂 """
        LMSCoursePage().click_ketang_unit(web_driver)

    def test_click_online_mode(self, native_driver):
        LMSCoursePage().click_online_mode(native_driver)

    def test_get_page_down(self, native_driver):
        LMSCoursePage().get_page_down(native_driver)
        time.sleep(2)

    def test_click_luke_room(self, native_driver):
        LMSCoursePage().click_luke_room(native_driver)

    def test_click_luke_onsite(self, native_driver):
        LMSCoursePage().click_luke_onsite(native_driver)

    def test_click_page_zhibo(self, native_driver):
        LMSCoursePage().click_page_zhibo(native_driver)

    def test_click_page_huifang(self, native_driver):
        LMSCoursePage().click_page_huifang(native_driver)

    def test_new_create_ketang_publish(self, native_driver):
        """发布"""
        LMSCoursePage().click_ketang_publish(native_driver)