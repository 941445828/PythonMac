# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 班级 相关元素定位
"""
# 创建班级相关
btn_create_class = ("创建班级btn", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[1]/AXButton[@AXTitle='CAccessibleStartWidget']/AXButton[@AXTitle='create class']")


# class下 tab
tab_chat = ("聊天tab", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXCheckBox[@AXTitle='聊天']")
tab_hw = ("作业tab", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXCheckBox[@AXTitle='作业']")
tab_course = ("作业tab", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXCheckBox[@AXTitle='课程']")


# LMS-班级 各tab
TabCourse = ("课程tab", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXCheckBox[@AXTitle='课程']")
TabScore = ("成绩tab", 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXCheckBox[@AXTitle='成绩']")
BtnReload = ("页面reload btn", 'XPaths', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXButton")