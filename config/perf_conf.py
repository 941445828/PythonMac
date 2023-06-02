# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: PC  性能测试  相关使用配置
"""


from config.utils import timeStamp

# 登录用户名和密码
LOGIN_USER_NAME = '18210190306'
LOGIN_PASS_WORD = 'e123456'

# 将课节创建在此课程下
CLASSNAME = 'PERF_TEST'

# 使用云盘下的文件夹
YUNPANFLODER = '课件'

"""
# 在线教室打开文件场景
"""
# 场景名称描述
story_name = '录课模式'
# APP版本号
pc_version = 'v5.0.0.19'
# 测试服务器名称
server = 'mac-intel'

# 性能数据保存--csv文件名称定义
cpu_csv_name = 'cpu_' + story_name + '_' + pc_version + '_' + server + '_' + timeStamp()
# print(cpu_csv_name)
mem_csv_name = 'mem_' + story_name + '_' + pc_version + '_' + server + '_' + timeStamp()
# print(mem_csv_name)

# 绘图生成文件名称配置
cpu_png_name = 'cpu_' + story_name + '_' + server + '_' + timeStamp()
# print(cpu_png_name)
mem_png_name = 'mem_' + story_name + '_' + server + '_' + timeStamp()
# print(mem_png_name)

# 打开的文件列表
open_files_setting = ['mp3.mp3', 'pgn.pgn', 'pptx.pptx', 'sgf.sgf', 'eda.eda', 'mp4.mp4']
# open_files_setting = ['声与热.edb', '别董大带声音的ppt.pptx',  '觉醒.flv', '凯叔声律启蒙.mp3', '内部推荐操作指南.pdf', '计数器.edlink']

