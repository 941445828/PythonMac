# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from config import *
import pyperclip
import pyautogui


def timeStamp():
    """
    获取时间戳
    :return:
    """
    timestamp = str(int(time.time()))
    # print(timestamp)
    return timestamp
# timeStamp()


def now_time():
    """
    获取当前时间点
    :return:
    """
    now = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d_%H:%M:%S')
    # print(now)
    return now
# now_time()


def get_cpu_csv_url(name):
    """
    文件地址: 收集cpu存放的csv url
    :param name:
    :return:
    """
    cpu_file_url = PROJECT_DIR + '/csv/' + str(name) + '.csv'
    return cpu_file_url


def get_mem_csv_url(name):
    """
    文件地址: 收集mem存放的csv url
    :param name:
    :return:
    """
    cpu_file_url = PROJECT_DIR + '/csv/' + str(name) + '.csv'
    return cpu_file_url


def get_cpu_png_url(name):
    """
    cpu.csv数据, 绘图生成的png url
    :param name:
    :return:
    """
    draw_png_url = PROJECT_DIR + '/chart/' + str(name) + '_' + '.png'
    return draw_png_url


def get_mem_png_url(name):
    """
    mem.csv数据, 绘图生成的png url
    :param name:
    :return:
    """
    draw_png_url = PROJECT_DIR + '/chart/' + str(name) + '_' + '.png'
    return draw_png_url


def copy_paste(content):
    """
    复制粘贴
    :param content:
    :return:
    """
    pyperclip.copy(content)
    pyautogui.hotkey('command', 'v')
