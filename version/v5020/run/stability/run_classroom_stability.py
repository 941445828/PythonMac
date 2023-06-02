# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 稳定性--教室内
"""


from config import *
from config import stability_conf
from config.updateConf import UpdateConfig
from config import utils
from functs.collect_perf import Collect


# 更新配置
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_yunpanfolder(folder=stability_conf.YUNPANFLODER)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)


if __name__ == '__main__':
    pytest.main(['-vs',
                 '-reruns=1', '-reruns-delay=2',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_Course.py::TestOnlineCourseEnterClassRoom'
                 ])
