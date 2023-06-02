# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:  给场景性能输入，执行绘图
"""
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
#  以上代码可以保证在任何时候都切换到当前执行脚本所在目录中, 解决ModuleNotFoundError: No module named 'config'


from config.perf_conf import cpu_png_name, mem_png_name
from config import perf_conf
from functs.drawFun import draw_chart
from config import *


def use_draw():
    # # 绘图
    search_key_cpu = 'cpu_' + perf_conf.story_name      # 根据场景名称搜索
    search_key_mem = 'mem_' + perf_conf.story_name
    draw_chart(PROJECT_DIR + '/csv/', search_key_cpu, cpu_png_name)      # 自定义图片名字
    draw_chart(PROJECT_DIR + '/csv/', search_key_mem, mem_png_name)      # 自定义图片名字


use_draw()
