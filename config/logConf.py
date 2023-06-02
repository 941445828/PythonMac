# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from config import *


LOG_FILE_URL = PROJECT_DIR + '/testlog/' + str(datetime.date.today()) + '.log'
# print(LOG_FILE_URL)
LOG_NAME = "ClassIn-PC-STORY"
LOG_SET_LEVEL = "DEBUG"
LOG_FORMAT = '%(asctime)s-%(levelname)s-%(filename)s - %(lineno)d - %(message)s'
