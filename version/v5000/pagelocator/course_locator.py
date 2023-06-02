# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 课程 相关元素定位
"""

# 添加课节button
Btn_Add_Course = ('添加课节button', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='ClassIn' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXSplitGroup[0]/AXGroup[0]/AXGroup[0]/AXGroup[0]/AXGroup[0]/AXButton[@AXTitle='添加课节']")

# 课节名称输入框
Text_Course = ('课节名称输入框', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXTextField")

# 教学模式
Course_Mode_Online = ('在线教室', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[0]")
Course_Mode_Wisdom = ('智慧教室', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[1]")

# 云端录课
Luke_Room = ('录制教室', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[2]")
Luke_Location = ('录制现场', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[3]")

# 网页直播
LiveStream = ('网页直播', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[@AXTitle='网页直播']")

# 网页回放
PlayBack = ('网页回放', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXCheckBox[@AXTitle='网页回放']")

# 创建课节button
Btn_Create = ('button创建', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXButton[@AXTitle='创建']")


# 进入教室相关
# 点击”上课“，进入教室内
Btn_Enter_Room = ("课程列表上的上课btn", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXButton[@AXTitle='进入教室']")

# 点击教室内的 “进入教室”
Btn_Enter = ('进入教室', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXFloatingWindow']/AXButton[@AXTitle='进入教室']")

# 点击录课提示的 “确定”
Sure = ('确定', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='提示' and @AXSubrole='AXDialog']/AXGroup[0]/AXButton[@AXTitle='确定']")

# 教室窗口的title
ClassRoomWin = ('教室内classroom窗口', 'XPaths', "/AXApplication[@AXTitle='ClassIn']/AXWindow")

# 点击录课提示的 “立即录课”
Luke = ('立即录课btn', 'XPath', "/AXButton[@AXTitle='立即录课']")


# ---LMS
# 课程活动列表H5页，【上课】btn
H5_Enter_Room = ('上课', 'XPaths', "//div[@class='flex flex-col text-right justify-center']/button")