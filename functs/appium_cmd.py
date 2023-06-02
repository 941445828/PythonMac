import os
import psutil
from handler.logHandler import logger
import time


def start_appium():
    cmd_str = 'open /Applications/AppiumForMac.app'
    os.system(cmd_str)
    time.sleep(5)


def get_appium_pid():
    pids = psutil.pids()  # 获取全部pid（list类型）
    pid_name = []  # 解析pids，获取所用程序的pid
    for pid in pids:
        try:
            p = psutil.Process(pid)
            pid_name.append("%d,%s" % (pid, p.name()))
        except Exception:
            logger.error('psutil.Process（）方法报错了！捕获')
    # print(pid_name)
    list_len = len(pid_name)
    for i in range(list_len):
        if 'AppiumForMac' in pid_name[i]:
            target_pid = pid_name[i].split(',')[0]
            # print(target_pid)
            # logger.info('获取到pid: {} '.format(target_pid))
            return target_pid
        else:
            continue


def kill_appium_pid():
    pid = get_appium_pid()
    if pid is None:
        return True
    else:
        use_str = 'kill -9 ' + pid
        print('AppiumForMac 已关闭！')
        logger.error('AppiumForMac 已关闭！')
        logger.error(use_str)
        os.system(use_str)
        time.sleep(5)
