# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 课节
"""
from config import *
from version.v5000.pagelocator import course_locator as course
from handler.eleHandler import find_element
from version.v5000.pageobject.onlineclassroom_page import OnLineClassRoomWin


class AddOnlineCoursePage:
    # 点击’添加课节‘button
    def click_addcourse_button(self, driver):
        ele = course.Btn_Add_Course
        ele_add = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_add).perform()

    # 输入课节名称
    def input_cousername(self, driver, course_name):
        ele = course.Text_Course
        ele_course_text = find_element(driver, ele[0], ele[1], ele[2])[0]
        ActionChains(driver).click(ele_course_text).perform()
        ele_course_text.clear()
        course_name = course_name.split('_')[0] + '_' + str(int(time.time()))
        ele_course_text.send_keys(course_name)

    # 选择在线教室模式
    def click_online_mode(self, driver):
        ele = course.Course_Mode_Online
        ele_mode = find_element(driver, ele[0], ele[1], ele[2])  # 在线教室
        ActionChains(driver).click(ele_mode).perform()

    # 选择智慧教室模式
    def click_wisdom_mode(self, driver):
        ele = course.Course_Mode_Wisdom
        ele_mode = find_element(driver, ele[0], ele[1], ele[2])  # 智慧教室
        ActionChains(driver).click(ele_mode).perform()

    # 勾选录课
    def click_lukeroom_mode(self, driver):
        ele = course.Luke_Room
        ele_luke = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_luke).perform()
        time.sleep(1)

    def click_lukelocation_mode(self, driver):
        ele = course.Luke_Location
        ele_luke = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_luke).perform()
        time.sleep(1)

    # 勾选直播
    def click_zhibo(self, driver):
        ele = course.LiveStream
        ele_zhibo = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_zhibo).perform()
        time.sleep(1)

    # 勾选回放
    def click_huifang(self, driver):
        ele = course.PlayBack
        ele_huifang = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_huifang).perform()
        time.sleep(1)

    # 点击创建button
    def click_create_button(self, driver):
        ele = course.Btn_Create
        ele_create = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_create).perform()


# 进入在线教室
    # 点击”上课“，进入教室内
    def click_shangke(self, driver):
        ele = course.Btn_Enter_Room
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_enter).perform()

    # 点击教室内的 “进入教室”
    def click_enter_classroom(self, driver):
        ele = course.Btn_Enter
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_enter).perform()

    # 点击录课提示的 “确定”
    def click_sure(self, driver):
        ele = course.Sure
        ele_sure = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_sure).perform()
        time.sleep(5)

    # 点击“立即录课”
    def click_luke(self, driver):
        ele = course.Luke
        # print(OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ele_class = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        # print(ele_class)
        ActionChains(driver).move_to_element(ele_class).click().perform()
        time.sleep(5)

    # 课程列表H5页，点击【上课】btn
    def click_btn_begin_class(self, driver):
        ele = course.H5_Enter_Room
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).click(ele_enter[-1]).perform()