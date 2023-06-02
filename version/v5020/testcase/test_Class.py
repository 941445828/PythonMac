# coding = utf-8
"""
@Author: sujie
@Create on: 2021
@Modify on：
@File: 创建班级、切换tab、
"""

from version.v5000.pageobject.class_page import ClassPage, LMSClassPage
from handler.yamlHandler import get_data


class TestUseTargetClass:
    def test_use_target_class(self, native_driver):
        """
        进入指定名称的班级
        """
        case = get_data('baseConf.yaml')[0]
        class_name = case['target_classname']
        ClassPage().click_target_class(native_driver, class_name)


class TestChangeTab(object):
    def test_change_tab(self, native_driver):
        """
        切换tab
        :param native_driver:
        :return:
        """
        ClassPage().click_course(native_driver)


# --- NEW LMS
class TestChangeCourseTab:
    def test_change_to_course(self, native_driver):
        LMSClassPage().click_course(native_driver)


class TestChangeScoreTab:
    def test_change_to_score(self, native_driver):
        LMSClassPage().click_score(native_driver)


class TestClassPageReload:
    def test_class_page_reload(self, native_driver):
        LMSClassPage().click_reload(native_driver)