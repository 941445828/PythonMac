# coding = utf-8
"""
@Author: sujie
@Create on: 2021
@Modify on：
@File: 课节相关
"""
from config import *
from version.v5000.pageobject.course_page import AddOnlineCoursePage
from handler.yamlHandler import get_data
from version.v5000 import *
from version.v5000.pageobject.lmsCourse_page import LMSCoursePage


class TestAddOnlineCourseLuke(object):
    # 点击“添加课节”
    def test_click_addcourse(self, native_driver):
        AddOnlineCoursePage().click_addcourse_button(native_driver)

    def test_enter_coursename(self, native_driver):
        # 填充 课节名称
        case = get_data('class.yaml')[0]
        AddOnlineCoursePage().input_cousername(native_driver, case['online_course_name'])

    def test_choose_coursemode(self, native_driver):
        # 选择教学模式
        AddOnlineCoursePage().click_online_mode(native_driver)

    def test_choose_lukeroome(self, native_driver):
        # 勾选云端录课
        AddOnlineCoursePage().click_lukeroom_mode(native_driver)

    def test_choose_lukelocation(self, native_driver):
        # 勾选云端录课
        AddOnlineCoursePage().click_lukelocation_mode(native_driver)

    def test_scroll(self, native_driver):
        # 滚动滚动条到最下方
        ActionChains(native_driver).key_down(Keys.PAGE_DOWN).perform()

    def test_choose_zhibo(self, native_driver):
        # 勾选网页直播
        AddOnlineCoursePage().click_zhibo(native_driver)

    def test_choose_huifang(self, native_driver):
        # 勾选网页回放
        AddOnlineCoursePage().click_huifang(native_driver)

    def test_create(self, native_driver):
        # 点击创建
        AddOnlineCoursePage().click_create_button(native_driver)
        time.sleep(5)


class TestAddOnlineCourseNoLuke(object):
    # 点击“添加课节”
    def test_click_addcourse(self, native_driver):
        AddOnlineCoursePage().click_addcourse_button(native_driver)

    def test_enter_coursename(self, native_driver):
        # 填充 课节名称
        case = get_data('class.yaml')[0]
        AddOnlineCoursePage().input_cousername(native_driver, case['online_course_name'])

    def test_choose_coursemode(self, native_driver):
        # 选择教学模式
        AddOnlineCoursePage().click_online_mode(native_driver)

    def test_scroll(self, native_driver):
        # 滚动滚动条到最下方
        ActionChains(native_driver).key_down(Keys.PAGE_DOWN).perform()

    def test_create(self, native_driver):
        # 点击创建
        AddOnlineCoursePage().click_create_button(native_driver)
        time.sleep(5)


class TestOnlineCourseEnterClassRoom(object):
    """ 进教室 """
    def test_click_begin_class(self, native_driver):
        # 点击上课
        AddOnlineCoursePage().click_shangke(native_driver)
        time.sleep(5)

    def test_enter_class(self, native_driver):
        # 点击教室内--进入教室
        AddOnlineCoursePage().click_enter_classroom(native_driver)
        time.sleep(5)


class TestOnlineCourseLuKeEnterEnsure:
    def test_luke_ensure(self, native_driver):
        # 点击录课提示的 “确定”
        AddOnlineCoursePage().click_sure(native_driver)

    def test_luke(self, native_driver):
        # 点击“立即录课”
        AddOnlineCoursePage().click_luke(native_driver)


# --- LMS
class TestEnterClassRoomH5:
    def test_switch_win_1(self, web_driver):
        get_new_page_special(web_driver, "&role=manager")

    def test_click_search_logo(self, web_driver):
        LMSCoursePage().click_search_logo(web_driver)

    def test_enter_search_content(self, web_driver):
        case = get_data('baseConf.yaml')[0]
        classname = case['target_classname']
        LMSCoursePage().enter_search_content(web_driver, classname, 5)

    def test_begin_class(self, web_driver):
        AddOnlineCoursePage().click_btn_begin_class(web_driver)
        time.sleep(5)

    def test_enter_classroom(self, native_driver):
        # 点击教室内--进入教室
        AddOnlineCoursePage().click_enter_classroom(native_driver)
        time.sleep(5)