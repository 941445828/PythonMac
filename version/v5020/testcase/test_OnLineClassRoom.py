# coding = utf-8
"""
@Author: sujie
@Create on: 2023-2
@Modify on：
@File: 在线教室相关
"""
from config import perf_conf
from version.v5010.pageobject.onlineclassroom_page import Tool_YunPan, OpenFile, Close_File, ToolRoster, ToolChat, ToolPen
from handler.yamlHandler import get_data
from version.v5010 import *


class TestOnlineCloseFiles:
    def test_close_files(self, native_driver):
        Close_File().get_files(native_driver)


class TestUseYunPan(object):
    def test_click_yunpan(self, native_driver):
        Tool_YunPan().click_tool_yunpan(native_driver)


class TestUseWenDang:
    def test_click_wendang(self, web_driver):
        time.sleep(2)
        get_new_page_special(web_driver, "inspector")
        OpenFile().click_wendang(web_driver)


class TestUseTargetFolder:
    def test_click_target_folder(self, web_driver):
        case = get_data('baseConf.yaml')[0]
        OpenFile().click_target_folder(web_driver, case['target_yunpan_folder'])


class TestUseTargetFolderGrid:
    def test_click_target_folder_grid(self, web_driver):
        case = get_data('baseConf.yaml')[0]
        OpenFile().click_target_folder_grid(web_driver, case['target_yunpan_folder'])


class TestChangeModelFileName:
    def test_click_order(self, web_driver):
        OpenFile().click_order(web_driver)

    def test_click_file_name_(self, web_driver):
        OpenFile().click_use_file_name(web_driver)


class TestOpenFile:
    def test_click_pdf_file(self, web_driver):
        OpenFile().click_target_file_grid(web_driver, '.pdf')
        time.sleep(10)

    def test_click_mp4_file(self, web_driver):
        OpenFile().click_target_file_grid(web_driver, '.mp4')
        time.sleep(10)

    def test_click_ppt_file(self, web_driver):
        OpenFile().click_target_file_grid(web_driver, '.ppt')
        time.sleep(10)


class TestRoster:
    def test_open_roster(self, native_driver):
        ToolRoster().click_roster_icon(native_driver)


class TestLunBo:
    def test_lunbo_perf(self, native_driver):
        TestRoster().test_open_roster(native_driver)
        ToolRoster().click_lunbo_start(native_driver)
        ToolRoster().close_roster_win(native_driver)


class TestChatSendTextAndPicFirst:
    def test_click_tool_chat(self, native_driver):
        ToolChat().click_tool_chat(native_driver, 12)

    def test_cut_pic(self, native_driver):
        ToolChat().click_cut_icon(native_driver)
        ToolChat().add_cut_pic(native_driver)
        ToolChat().click_cut_pic_ensure(native_driver)

    def test_click_edit_chat(self, native_driver):
        ToolChat().click_chat_text(native_driver)

    def test_edit_chat_text(self, native_driver):
        ToolChat().chat_add_content(native_driver)

    def test_send_chat(self, native_driver):
        ToolChat().click_chat_send(native_driver)

    def test_chat_win_close(self, native_driver):
        ToolChat().click_chat_win_close(native_driver, 3)


class TestChatSendTextAndPicSecond:
    def test_click_tool_chat(self, native_driver):
        ToolChat().click_tool_chat(native_driver, 12)

    def test_cut_pic(self, native_driver):
        ToolChat().click_cut_icon(native_driver)
        ToolChat().add_cut_pic(native_driver)
        ToolChat().click_cut_pic_ensure(native_driver)

    def test_click_edit_chat(self, native_driver):
        ToolChat().click_chat_text(native_driver)

    def test_edit_chat_text(self, native_driver):
        ToolChat().chat_add_content(native_driver)

    def test_send_chat(self, native_driver):
        ToolChat().click_chat_send(native_driver)

    def test_chat_win_close(self, native_driver):
        ToolChat().click_chat_win_close(native_driver, 4)


class TestChatSendTextAndPicThird:
    def test_click_tool_chat(self, native_driver):
        ToolChat().click_tool_chat(native_driver, 12)

    def test_cut_pic(self, native_driver):
        ToolChat().click_cut_icon(native_driver)
        ToolChat().add_cut_pic(native_driver)
        ToolChat().click_cut_pic_ensure(native_driver)

    def test_click_edit_chat(self, native_driver):
        ToolChat().click_chat_text(native_driver)

    def test_edit_chat_text(self, native_driver):
        ToolChat().chat_add_content(native_driver)

    def test_send_chat(self, native_driver):
        ToolChat().click_chat_send(native_driver)

    def test_chat_win_close(self, native_driver):
        ToolChat().click_chat_win_close(native_driver, 5)


class TestToolPen:
    def test_click_tool_pen(self, native_driver):
        ToolPen().click_tool_pan(native_driver)



