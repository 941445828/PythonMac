# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from config import *
from appium import webdriver as nativedriver
from selenium import webdriver as webviewdriver
from handler.logHandler import logger


@pytest.fixture(scope='session')
def native_driver():
    global driver
    desiredCapabilities = {
        'platformName': "Mac",
        'newCommandTimeout': 60,
        'showServerLogs': True
    }
    if desiredCapabilities is not None:
        try:
            driver = nativedriver.Remote(command_executor='http://127.0.0.1:4622/wd/hub', desired_capabilities=desiredCapabilities)
            driver.get(APP)     # 启动APP
        except Exception as msg:
            logger.error(msg)
            logger.error("====== nativedriver 连接失败！ ======")
        else:
            logger.info("====== nativedriver 已连接 ======")
            time.sleep(5)
            yield driver
            time.sleep(2)
            driver.quit()
            logger.info("====== nativedriver已断开 ======")
            return driver


@pytest.fixture(scope="session")
def web_driver():
    try:
        webview_page_url = INSPECT_URL
        chrome_options = webviewdriver.ChromeOptions()
        chrome_options.debugger_address = webview_page_url
        webdriver = webviewdriver.Chrome(WEBVIEW_DRIVER_URL, options=chrome_options)
        time.sleep(2)
    except Exception as e:
        logger.error('webviewdriver 启动失败！ {}'.format(e))
        logger.error(e)
    else:
        logger.info("====== webviewdriver 已连接 ======")
        time.sleep(5)
        yield webdriver
        time.sleep(2)
        webdriver.quit()
        logger.info("====== webdriver已断开 ======")
        return webdriver


@pytest.fixture(scope="function")
def get_function_name(request):
    function_name = request.function.__name__
    logger.info('运行方法>>>>>：{}'.format(function_name))
    yield function_name