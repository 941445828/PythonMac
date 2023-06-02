# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 班级
"""
from config import *
from version.v5040.pagelocator import class_locator as Class
from handler.eleHandler import find_element


class ClassPage(object):
    def click_target_class(self, driver, target_classname):
        ele_xpath = "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[1]/AXGroup[0]/AXList[0]/AXStaticText[@AXTitle='"+target_classname+"']"
        ele_class = find_element(driver, "使用指定的班级：" + target_classname, "XPath", ele_xpath)
        ActionChains(driver).move_to_element(ele_class).click().perform()

    def click_course(self, driver):
        ele = Class.tab_course
        ele_tab = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_tab).click().perform()


# ---LMS
class LMSClassPage:
    def click_course(self, driver):
        ele = Class.TabCourse
        ele_tab = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_tab).click().perform()

    def click_score(self, driver):
        ele = Class.TabScore
        ele_tab = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_tab).click().perform()

    def click_reload(self, driver):
        ele = Class.BtnReload
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_btn[1]).click().perform()
        time.sleep(2)





