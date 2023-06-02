# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from handler.yamlHandler import YamlMethod, get_data
from handler.logHandler import logger


# 更新基础配置
class UpdateConfig:
    def __init__(self,  *args, **kwargs):
        pass

    # 调用，更新配置
    # def updateConfig(self, app=None, name=None, pw=None, classname=None):
    #     # self.get_app_version(app)
    #     self.get_login(name, pw)
    #     self.get_classname(classname)

    # 获取要测试用的APP版本
    def get_app_version(self, app):
        case = get_data('baseConf.yaml')[0]
        case['app_url'] = app
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("客户端使用版本： {}".format(app))
        return app

    # 获取要测试用的webdriver版本
    def get_webdriver_version(self, webdriver_version):
        case = get_data('baseConf.yaml')[0]
        case['webdriver_version'] = webdriver_version
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("webdriver使用版本： {}".format(webdriver_version))
        return webdriver_version

    # 获取登录的用户名密码
    def get_login(self, name, pw):
        case = get_data('baseConf.yaml')[0]
        case['content_username'] = name
        case['content_pwd'] = pw
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("登录使用用户名： {}， 密码： {}".format(name, pw))
        return name, pw

    # 获取要使用班级名称
    def get_classname(self, classname):
        case = get_data('baseConf.yaml')[0]
        case['target_classname'] = classname
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("功能运行名称是：{}的班群下".format(classname))
        return classname

    # 获取要使用云盘下的文件夹名称
    def get_yunpanfolder(self, folder):
        case = get_data('baseConf.yaml')[0]
        case['target_yunpan_folder'] = folder
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("功能运行使用的云盘文件夹：{}".format(folder))
        return folder

    # 获取要使用班级名称
    def get_classforcopy(self, classname):
        case = get_data('baseConf.yaml')[0]
        case['class_for_copy'] = classname
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("被复制使用的班级：{}".format(classname))
        return classname
