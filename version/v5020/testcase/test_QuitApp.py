# coding = utf-8
"""
@Author: sujie
@Create on: 2021
@Modify on：
@File: 退出APP
"""
from version.v5000.pageobject.setting_page import SettingPage, QuitAppPage


class TestQuitApp:
    def test_click_setting(self, native_driver, get_function_name):
        SettingPage().click_setting(native_driver)

    def test_quit(self, native_driver, get_function_name):
        QuitAppPage().click_quit(native_driver)

    def test_quit_sure(self, native_driver, get_function_name):
        QuitAppPage().click_sure(native_driver)