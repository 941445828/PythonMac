# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:  设置页面相关
"""
from config import *
from version.v5000.pagelocator import setting_locator as Setting
from handler.eleHandler import find_element


class SettingPage:
    def click_setting(self, driver):
        ele = Setting.Setting
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_setting).click().perform()


class QuitAppPage:
    def click_quit(self, driver):
        ele = Setting.Exit
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_setting).click().perform()

    def click_sure(self, driver):
        ele = Setting.Exit_Sure
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_setting).click().perform()

