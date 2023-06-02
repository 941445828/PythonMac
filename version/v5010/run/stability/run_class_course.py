# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: LMS课程下各活动新建&编辑
"""


from config import *
from config import stability_conf
from config.updateConf import UpdateConfig
from functs import killPid
from version.v5000 import *


# 更新配置
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)
UpdateConfig().get_yunpanfolder(folder=stability_conf.YUNPANFLODER)
UpdateConfig().get_classforcopy(classname=stability_conf.CLASSFORCOPY)


def run_course():
    killPid.kill_pid()
    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_Class.py::TestUseTargetClass',  # 使用班群
                 '../../testcase/test_Class.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/class/test_Create_UnitTopic.py::TestCreateUnitTopic',
                 '../../testcase/class/test_Create_KeTang.py::TestCreateKeTang',  # 创建课堂
                 '../../testcase/class/test_Create_Luboke.py::TestCreateLuboke',
                 '../../testcase/class/test_Create_Homework.py::TestCreateHomework',
                 '../../testcase/class/test_Create_Exam.py::TestCreateExam',
                 '../../testcase/class/test_Create_Discuss.py::TestCreateDiscuss',
                 '../../testcase/class/test_Create_LearningMaterials.py::TestCreateLearningMaterials',
                 '../../testcase/class/test_CopyOtherClassActivities.py::TestCopyOtherClassActivities',
                 '../../testcase/test_Class.py::TestChangeScoreTab',  # 切换到成绩tab
                 '../../testcase/class/test_CheckScore.py::TestCheckScore',
                 '../../testcase/test_Class.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/class/test_Edit_KeTang.py::TestEditKeTang',  # 编辑课堂
                 '../../testcase/class/test_Edit_Luboke.py::TestEditLuboke',
                 '../../testcase/class/test_Edit_Homework.py::TestEditHomework',
                 '../../testcase/class/test_Edit_Exam.py::TestEditExam',
                 '../../testcase/class/test_Edit_Discuss.py::TestEditDiscuss',
                 '../../testcase/class/test_Edit_LearnMaterials.py::TestEditLearningMaterials',
                 '../../testcase/test_QuitApp.py::TestQuitApp'
                 ])


while True:
    run_course()