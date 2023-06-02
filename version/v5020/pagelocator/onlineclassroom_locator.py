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




# # 举手上台区域
# HandUp_icon = ('', '', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='Classroom_187718_266267' and @AXSubrole='AXStandardWindow']")


#   聊天区域

Chat_Cut_Icon = ('聊天框上的截图icon', 'XPath', "/AXGroup[0]/AXSplitGroup/AXButton[1]")
Chat_Text = ('聊天框输入框', 'XPath', "/AXGroup[0]/AXSplitGroup/AXTextArea")
Chat_Emoji_Btn = ('聊天框表情btn', 'XPath', "/AXGroup[0]/AXSplitGroup/AXButton[0]")
Chat_Send_Btn = ('聊天框发送btn', 'XPath', "/AXGroup[0]/AXSplitGroup/AXButton[2]")


def chat_win_close(i):
    # 教室内，聊天窗口的关闭btn，性能测试脚本用--因打开的课节数量不同，btn的下标+1
    Chat_Win_Close = ('聊天框关闭X', 'XPath', "/AXButton[" + str(i) + "]")
    return Chat_Win_Close

# 花名册
Option_lunbo_start = ('开启轮播option', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='花名册' and @AXSubrole='AXFloatingWindow']/AXCheckBox[@AXTitle='开启']")
Roster_Win_close_btn = ('花名册窗口关闭btn', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='花名册' and @AXSubrole='AXFloatingWindow']/AXButton[0]")

# 云盘
YunPan_Order = ('云盘-排序', 'XPath', "//div[text()='排序']")
YunPan_Order_FileName = ('云盘-排序-文件名称', 'XPath', "//span[text()='文件名称']")
# "(//div[text()='.pdf'])[last()]"  # 网格
# "(//div[span='.pdf'])[last()]"  # 列表
# "//div[@class='flex align-center justify-center index_switch__RCqrP ant-tooltip-open']"



######### 学生操作
stu_cancel = ('学生课后评价窗上的取消', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXButton[@AXTitle='取消']")