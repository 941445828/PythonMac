# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 在线教室内
"""
from config import *
from version.v5010.pagelocator import onlineclassroom_locator as onlineclassroom
from handler.eleHandler import find_element
import pyautogui
import random
from handler.yamlHandler import get_data
from config import utils


class OnLineClassRoomWin:
    def get_screen_size(self):
        screen_x, screen_y = pyautogui.size()
        # print(screen_x, screen_y)  # 1440 900
        x = random.randint(50, screen_x-80)
        y = random.randint(200, screen_y-40)
        return x, y

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
        """2023.2.10---云盘更新，此xpath找不到文件夹了"""
        ele_xpath = "//div[contains(text(),'" + folder_name + "')]"
        ele_folder = find_element(driver, '文件夹名称', 'XPath', ele_xpath)
        ele_folder.click()

    def click_target_folder(self, driver, folder_name):
        ele = "//div/span[contains(text(),'" + folder_name + "')]"
        ele_folder = find_element(driver, '文件夹名称', 'XPath', ele)
        ele_folder.click()

    def click_target_folder_grid(self, driver, folder_name):
        ele = "(//*[div='" + folder_name + "'])[last()]"
        ele_folder = find_element(driver, '网格视图下，文件夹名称', 'XPath', ele)
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

    def click_target_file(self, driver, file_kind):
        """ file_kind传参要求如: .pdf .pm4  """
        # "//div[span='.pdf']"
        # (// div[span='.pdf'])[1]  第一个
        ele_xpath = "//div[span='" + file_kind + "']"
        ele_file = find_element(driver, '打开文件类型：' + file_kind, 'XPaths', ele_xpath)
        ele_file[0].click()


    def click_order(self, driver):
        ele = onlineclassroom.YunPan_Order
        ele_order = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_order).click().perform()

    def click_use_file_name(self, driver):
        ele = onlineclassroom.YunPan_Order_FileName
        ele_xpath = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_xpath).click().perform()

    def click_target_file_grid(self, driver, file_kind):
        time.sleep(2)
        ele = "(//div[text()='" + file_kind + "'])[last()]"
        ele_file = find_element(driver, '网格视图下，打开文件类型：' + file_kind, 'XPaths', ele)
        ele_file[0].click()


class Close_File:
    def get_files(self, driver):
        ele = onlineclassroom.File
        # ele_f = OnLineClassRoomWin().get_classroom_window(driver) + ele[2]
        # print(ele_f)
        # ele_file = find_element(driver, ele[0], ele[1], ele_f)
        # print(len(ele_file))
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        # print(len(ele_btn))
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


class ToolChat:
    def click_tool_chat(self, driver, i):
        # 点击工具栏-聊天
        # ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[11]).click().perform()
        ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[i]).click().perform()

    def click_cut_icon(self, driver):
        ele = onlineclassroom.Chat_Cut_Icon
        ele_btn = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ActionChains(driver).move_to_element(ele_btn).click().perform()

    def add_cut_pic(self, driver):
        x = OnLineClassRoomWin().get_screen_size()[0]
        y = OnLineClassRoomWin().get_screen_size()[1]
        pyautogui.moveTo(x, y)
        m = OnLineClassRoomWin().get_screen_size()[0]
        n = OnLineClassRoomWin().get_screen_size()[1]
        pyautogui.dragTo(m, n, duration=2, button='left')
        time.sleep(2)

    def click_cut_pic_ensure(self, driver):
        ActionChains(driver).double_click().perform()

    def click_chat_text(self, driver):
        ele = onlineclassroom.Chat_Text
        ele_text = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ActionChains(driver).move_to_element(ele_text).click().perform()

    def chat_add_content(self, driver):
        """发送聊天内容： 从content list中，随机选一条文字，发送 """
        content = random.choice(get_data('baseConf.yaml')[0]['online_chat_content'])
        utils.copy_paste(content)
        time.sleep(2)

    def click_chat_send(self, driver):
        ele = onlineclassroom.Chat_Send_Btn
        ele_btn = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ActionChains(driver).move_to_element(ele_btn).click().perform()

    def click_chat_win_close(self, driver, i):
        ele = onlineclassroom.chat_win_close(i)
        ele_close = find_element(driver, ele[0], ele[1], OnLineClassRoomWin().get_classroom_window(driver) + ele[2])
        ActionChains(driver).move_to_element(ele_close).click().perform()


class ToolRoster:
    def click_roster_icon(self, driver):
        ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[12]).click().perform()

    def click_lunbo_start(self, driver):
        ele = onlineclassroom.Option_lunbo_start
        ele_option = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_option).click().perform()

    def close_roster_win(self, driver):
        ele = onlineclassroom.Roster_Win_close_btn
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_btn).click().perform()


class ToolPen:
    def click_tool_pan(self, driver):
        ActionChains(driver).move_to_element(OnLineClassRoomToolBarWrapper().get_toolbarwrappers(driver)[2]).click().perform()





####### 学生端
class StudentQuitOnlineRoom:
    def click_cancel(self, driver):
        ele = onlineclassroom.stu_cancel
        ele_cancel = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).move_to_element(ele_cancel).click().perform()
