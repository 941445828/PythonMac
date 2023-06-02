from time import sleep
import os
import psutil
from functs import getPid
from handler.logHandler import logger
import time


def kill_pid():
    pid = getPid.get_pid()

    if pid is None:
        return True
        # logger.info('无ClassIn.exe运行中！')
    else:
        use_str = 'kill -9 ' + pid
        print('ClassIn.exe 进程存在，将关闭进程！')
        logger.error('ClassIn.exe 进程存在，将关闭以下： ')
        logger.error(use_str)
        os.system(use_str)
        time.sleep(5)


# kill_pid()
