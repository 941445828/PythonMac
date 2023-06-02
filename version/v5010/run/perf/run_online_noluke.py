# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: LMS合并后的客户端UI
场景描述：登录--进入班级--创建课节（非录课模式）--进入教室--打开多个课件（间隔1分组）--课件全部打开后在教室内停留60s--退出教室--退出教室，获取cpu/mem
"""


from config import *
from config import perf_conf
from config.updateConf import UpdateConfig
from config import utils
from functs.getPerfData import Collect
import threading


def noluke():
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_yunpanfolder(folder=perf_conf.YUNPANFLODER)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)

    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_Class.py::TestUseTargetClass',
                 '../../testcase/test_Class.py::TestChangeCourseTab',
                 '../../testcase/class/test_Create_KeTang.py::TestCreateNoLuKeKeTang',
                 '../../testcase/test_Course.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/perf/test_OnLine_ClassRoom.py::TestOnLineOpenFiles',
                 '../../testcase/test_Quit_ClassRoom.py::TestQuitOnlineClassRoom',
                 '../../testcase/test_QuitApp.py::TestQuitApp'
                 ])


# noluke()


def collect():
    cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
    # print(cpu_file_url)
    mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
    # print(mem_file_url)
    Collect().get_data(cpu_file_url, mem_file_url)


# collect()


def run_noluke():
    t1 = threading.Thread(target=noluke)
    t2 = threading.Thread(target=collect)

    t1.start()
    t2.start()


if __name__ == "__main__":
    run_noluke()
