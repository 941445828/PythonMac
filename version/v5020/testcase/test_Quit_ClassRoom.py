# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 录课&非录课模式，全员下课，都有弹窗提示”确定下课？“
录课模式， 仅自己离开，有弹窗提示”确定关闭教室？“
非录课模式，仅自己开始，无弹窗提示，直接退出教室
"""
import allure
from version.v5010.pageobject.onlineclassroom_page import QuitClassRoomPage, StudentQuitOnlineRoom


@allure.feature("班级")
@allure.story("测试-班级-退出在线教室--全员下课")
class TestQuitOnlineClassRoom:
    """录课&非录课模式--全员下课"""
    @allure.title('退出(在线教室)--全员下课')
    @allure.description("测试：退出(在线教室)--全员下课")
    def test_quit(self, native_driver, get_function_name):
        QuitClassRoomPage().click_win_close_btn(native_driver)

    def test_quit_all(self, native_driver, get_function_name):
        QuitClassRoomPage().click_all_off(native_driver)
        QuitClassRoomPage().click_sure(native_driver)


class TestStudentQuitOnlineClassRoom:
    def test_quit(self, native_driver):
        QuitClassRoomPage().click_win_close_btn(native_driver)

    def test_quit_appraise(self, native_driver):
        StudentQuitOnlineRoom().click_cancel(native_driver)
