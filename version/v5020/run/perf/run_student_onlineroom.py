# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 2023/2, 性能场景细化, 学生端
场景描述： https://www.notion.so/eeoof/2-981df8625a9c4c3ab15fd576ea4ed817

"""


from config import *
from config import perf_conf
from config.updateConf import UpdateConfig
from config import utils
from functs.getPerfData import Collect
import threading


def luke():
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_yunpanfolder(folder=perf_conf.YUNPANFLODER)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)

    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_Class.py::TestUseTargetClass',
                 '../../testcase/test_Class.py::TestChangeCourseTab',
                 '../../testcase/test_Course.py::TestEnterClassRoomH5',  # 进入教室内

                 # 举手功能开启
                        ######   举手  元素找不到
                 '../../testcase/test_Quit_ClassRoom.py::TestStudentQuitOnlineClassRoom',
                 '../../testcase/test_QuitApp.py::TestQuitApp'
                 ])


luke()


# def collect():
#     cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
#     mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
#     Collect().get_data(cpu_file_url, mem_file_url)
#
#
# # collect()
#
#
# def run_luke():
#     t1 = threading.Thread(target=luke)
#     t2 = threading.Thread(target=collect)
#
#     t1.start()
#     t2.start()
#
#
# if __name__ == "__main__":
#     run_luke()
#
#
#
