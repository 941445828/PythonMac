# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 在线教室 相关元素定位
"""
# 所有存在的窗口
All_Wins = ('获取所有窗口', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/AXWindow")


# 教室窗口的title
ClassRoomWin = ('教室内classroom窗口', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/AXWindow")

# 教室内，所有属性是CheckBox
CheckBox = ('教室内所有属性是CheckBox', 'XPaths', "/AXCheckBox")

# 教室内，所有属性是Button
Button = ('教室内所有属性是Button', 'XPaths', "/AXButton")

# 教室内，工具栏 toolbarwrapper
toolbarwrapper = ('教室内工具栏', 'XPaths', "/descendant::*[@AXTitle='ToolbarWrapper']/descendant::*")

# 教室内，打开的文件
# File = ('打开的课件上的button', 'XPaths', "/descendant::[@AXTitle='course_mp3.mp3']/descendant::*/AXButton")  # 定位不到
# File = ('打开的课件上的button', 'XPaths', "/descendant::[@AXTitle='course_mp3.mp3']/descendant::*/AXButton")
# File = ('打开的课件上的button', 'XPaths', "/descendant::*/AXButton[@AXTitle='course_mp3.mp3']")
# File = ('打开的课件上的button', 'XPaths', "/descendant::/AXButton[@AXTitle='course_mp3.mp3']")
# File = ('打开的课件上的button', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/descendant::*/AXButton[@AXTitle='course_mp3.mp3']")
File = ('打开的课件上的button', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/descendant::*/[@AXTitle='course_mp3.mp3']/AXButton")

# H5--定位‘文档’
WenDang = ('文档', 'XPath', "//div[span='文档']")

# 教室关闭'X'
Win_Close_Btn = ("教室关闭窗口的'X'", 'XPaths', "/descendant::AXButton")

# 全员下课
All_Off_Btn = ('全员下课Button', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/descendant::*/AXButton[@AXTitle='全员下课']")

# 仅自己离开
One_Off_Btn = ('全员下课Button', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/descendant::*/AXButton[@AXTitle='仅自己离开']")

# 退出教室提示框上的确定
Sure_Btn = ('退出教室提示框上的确定', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/descendant::*/AXButton[@AXTitle='确定']")
