# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.login_page import LoginPage
from handler.yamlHandler import get_data
import allure


@allure.feature("登录")
@allure.story("测试--ClassIn登录")
class TestLogin:
    @allure.title('登录')
    @allure.description("输入正确的用户名+密码，登录成功")
    def test_login(self, native_driver, get_function_name):
        case = get_data('baseConf.yaml')[0]
        # logger.info("login--用例 {}：".format(case))
        LoginPage().input_username(native_driver, case['content_username'])
        LoginPage().input_pwd(native_driver, case['content_pwd'])
        LoginPage().click_button_login(native_driver)

