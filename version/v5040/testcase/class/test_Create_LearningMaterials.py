# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
"""
from version.v5040.pageobject.lmsCourse_page import LMSCoursePage
from version.v5040 import *


class TestCreateLearningMaterials:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "&role=manager")

    def test_click_create_H5(self, web_driver):
        """ 课程tab下，H5上的【新建】"""
        LMSCoursePage().click_H5_create(web_driver)

    def test_new_create_learning_materials(self, web_driver):
        LMSCoursePage().click_learning(web_driver)

    def test_switch_win_2(self, web_driver):
        get_new_page_special(web_driver, "/material/")

    def test_learning_materials_title(self, web_driver):
        LMSCoursePage().enter_learn_title(web_driver)

    def test_learning_materials_content(self, web_driver):
        LMSCoursePage().enter_learn_content(web_driver)

    def test_learning_materials_publish(self, web_driver):
        LMSCoursePage().click_publish_btn(web_driver)
