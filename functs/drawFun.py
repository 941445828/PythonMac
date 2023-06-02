# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 方法:绘制图表
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from functs.readPerfData import read_data
from config import utils, perf_conf
import os
from config.perf_conf import cpu_png_name, mem_png_name
from config import *


# import matplotlib
#
# # 查找字体路径
# print(matplotlib.matplotlib_fname())
# # 查找字体缓存路径
# print(matplotlib.get_cachedir())


# 统计，要绘入图的所有文件
def get_files(folder_path, search_file):
    file_list = []
    files = os.listdir(folder_path)
    # print(files)
    for file in files:
        cur_path = os.path.join(folder_path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            get_files(cur_path, search_file)
        else:
            # 判断是否是需要的文件
            if search_file in file:
                file = folder_path + file
                file_list.append(file)
    # print(file_list)
    return file_list
# get_files('/Users/testeeo/Documents/mac_story/csv/', 'cpu_录课模式')


# 绘图
def draw_chart(path, search, png_name):
    files = get_files(path, search)
    files_count = len(files)
    # print(files_count)
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    for i in range(files_count):  # i 文件数量
        file_url = get_files(path, search)[i]
        x_len = len(read_data(files[i]))
        x = np.arange(1, x_len+1)
        y = []
        file = read_data(files[i])  # 依次解析每个文件
        for j in range(len(file)):  # j 文件行数
            if 'cpu' in search:
                y.append(float(file[j]))

            elif 'mem' in search:
                y.append(float(file[j]))

        ax.plot(x, y, label=file_url)
    if search == 'cpu':
        ax.set_ylabel('cpu使用率 %')
        ax.set_title('CPU使用情况')
    elif search == 'mem':
        ax.set_ylabel('内存占用量 MB')
        ax.set_title('内存使用情况')
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 识别字体

    plt.rc('axes', unicode_minus=False)
    ax.set_xlabel('请求次数（1S/次）')
    ax.legend()
    if 'cpu' in search:
        plt.savefig(utils.get_cpu_png_url(png_name))
    elif 'mem' in search:
        plt.savefig(utils.get_mem_png_url(png_name))
    # plt.show()  # 注销掉之后, 不弹图片


# search_key_cpu = 'cpu_' + perf_conf.story_name      # 根据场景名称搜索
# search_key_mem = 'mem_' + perf_conf.story_name
# draw_chart(PROJECT_DIR + '/csv/', search_key_cpu, cpu_png_name)      # 自定义图片名字
# draw_chart(PROJECT_DIR + '/csv/', search_key_mem, mem_png_name)      # 自定义图片名字
