# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 登录页面
"""
from config import *
from version.v5000.pagelocator import login_locator as Login
from handler.eleHandler import find_element


class LoginPage:
    def input_username(self, driver, user_name):
        """
        获取元素-用户名，并输入内容
        :param driver:
        :param user_name:
        :return:
        """
        ele = Login.UserName
        ele_username = find_element(driver, ele[0], ele[1], ele[2])
        # 填充： 避免搜狗输入法
        ActionChains(driver).move_to_element(ele_username).click().perform()
        # 方法一：
        ActionChains(driver).send_keys(Keys.COMMAND, 'a').perform()
        pyperclip.copy(user_name)
        pyautogui.hotkey('command', 'v')
        # 方法二：
        # pyautogui.hotkey('command', 'a')
        # ActionChains(driver).click(ele_username).send_keys(user_name).perform()

    def input_pwd(self, driver, p_w_d):
        """
        获取元素-密码，并填充
        :param driver:
        :param p_w_d:
        :return:
        """
        ele = Login.PassWord
        ele_pwd = find_element(driver, ele[0], ele[1], ele[2])
        # 填充
        ActionChains(driver).move_to_element(ele_pwd).click().perform()
        ele_pwd.send_keys(p_w_d)

    def click_button_login(self, driver, ):
        """
        获取元素-btn登录
        :param driver:
        :return:
        """
        ele = Login.LoginButton
        ele_loginbutton = find_element(driver, ele[0], ele[1], ele[2])
        # 点击
        ActionChains(driver).move_to_element(ele_loginbutton).click().perform()
        time.sleep(5)
