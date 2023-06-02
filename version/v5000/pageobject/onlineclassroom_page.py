# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 在线教室内
"""
from config import *
from version.v5000.pagelocator import onlineclassroom_locator as onlineclassroom
from handler.eleHandler import find_element


class OnLineClassRoomWin:
    def get_all_wins(self, driver):
        ele = onlineclassroom.ClassRoomWin
        ele_wins = find_element(driver, ele[0], ele[1], ele[2])
        return ele_wins

    def get_classroom_window(self, driver):
        ele_win = self.get_all_wins(driver)[0]
        # print(ele_win)
        classroom_id = ele_win.get_attribute('AXTitle')
        # print(ele_win.get_attribute('AXTitle'))
        # print("/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='" + classroom_id + "' and @AXSubrole='AXStandardWindow']")
        return "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='" + classroom_id + "' and @AXSubrole='AXStandardWindow']"


class OnLineClassRoomToolBarWrapper:
    def get_toolbarwrappers(self, driver):
        ele = onlineclassroom.toolbarwrapper
        ele_tools = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        return ele_tools


class Tool_Click:
    def click_tool_click(self, driver):
        # 点击工具栏--'点击'
        ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[0]).click().perform()


class Tool_YunPan:
    def click_tool_yunpan(self, driver):
        # 点击工具栏--'云盘'
        ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[7]).click().perform()


class OpenFile:
    def click_wendang(self, driver):
        ele = onlineclassroom.WenDang
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        ele_win.click()

    def click_folder(self, driver, folder_name):
        ele_xpath = "//div[contains(text(),'" + folder_name +"')]"
        ele_folder = find_element(driver, '文件夹名称', 'XPath', ele_xpath)
        ele_folder.click()

    def click_file(self, driver, file):
        if file == 'doc.doc' or file == 'docx.docx':
            ele = "//div[contains(text(),'" + file.split('.')[0] + "')]"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPaths', ele)[1]
        else:
            ele = "//div[contains(text(),'" + file.split('.')[0] + "')]"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPath', ele)
        time.sleep(1)
        ele_file.click()


class Close_File:
    def get_files(self, driver):
        ele = onlineclassroom.File
        # ele_f = OnLineClassRoomWin().get_classroom_window(driver) + ele[2]
        # print(ele_f)
        # ele_file = find_element(driver, ele[0], ele[1], ele_f)
        # print(len(ele_file))
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        print(len(ele_btn))
        ActionChains(driver).move_to_element(ele_btn[-1]).click().perform()


class QuitClassRoomPage:
    def click_win_close_btn(self, driver):
        ele = onlineclassroom.Win_Close_Btn
        ele_btn = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ActionChains(driver).move_to_element(ele_btn[-1]).click().perform()


    def click_all_off(self, driver):
        ele = onlineclassroom.All_Off_Btn
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_btn[0]).click().perform()


    def click_sure(self, driver):
        ele = onlineclassroom.Sure_Btn
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_btn[0]).click().perform()


