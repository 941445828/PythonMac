# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: macOS -- 收集cpu、mem
"""
import time
import os
from functs.getPid import get_pid
from config import utils
from handler.logHandler import logger


class Collect:
    def get_data(self, cpu_file_url, mem_file_url):
        # cmd = "ps -v " + pid + " | awk 'NR==2 {print $3,$7,$8,$11,$12}'"
        # cmd_get_cpu = "ps -v " + pid + " | awk 'NR==2 {print $11}'"
        # cmd_get_rss = "ps -v " + pid + " | awk 'NR==2 {print $8}'"
        time.sleep(1)   # 确保先执行login，再开始收集数据
        try:
            while True:
                pid = get_pid()
                # 获取%CPU,
                cmd_get_cpu = "ps -v " + pid + " | awk 'NR==2 {print $11}' >> " + cpu_file_url
                os.system(cmd_get_cpu)
                # 获取RSS,单位KB
                cmd_get_rss = "ps -v " + pid + " | awk 'NR==2 {print $8}' >> " + mem_file_url
                os.system(cmd_get_rss)
                time.sleep(1)   # 1s收取一次
                print(time.time())
        except Exception as e:
            logger.error(e)


# Collect().get_data('/Users/testeeo/Documents/mac_story/csv/cpu_录课模式.csv', '/Users/testeeo/Documents/mac_story/csv/mem_录课模式.csv')

