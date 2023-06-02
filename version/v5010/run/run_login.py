# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 登录
"""
from config import *
from config import perf_conf
from config.updateConf import UpdateConfig


def start_run():
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)
    pytest.main(['-vsq',
                 '../testcase/test_Login.py'
                 ])


start_run()
