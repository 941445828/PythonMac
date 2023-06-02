# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: LMS版本，班级-课程
"""

# 公用
H5_Create = ('课程tab下的【新建】', 'XPath', '//span[text()= "新建"]')
# 公用 各活动发布btn
PublishBtn = ('活动发布btn', 'XPath', '//span[text()="发布"]')   # 单元主题、录播课、作业、讨论、学习资料。 测验的与这几个不一样


# 新建课堂
Btn_KeTang = ('新建课堂icon', 'XPath', '(//div[text()="课堂"])[1]')
Btn_KeTang_Unit = ('单元下新建课堂Btn', 'XPath', '(//div[text()="课堂"])[2]')
KeTangName = ('课堂名称填充', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXTextField[0]")
KeTangOnlineMode = ('在线教室模式', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXRadioButton[0]")
KeTangWisdomMode = ('智慧教室模式', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXRadioButton[1]")
LuKeRoom = ('录制教室', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXStaticText[14]")
LukeOnSite = ('录制现场', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXStaticText[16]")
PageZhiBo = ('网页直播', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXStaticText[@AXValue='网页直播']")
PageHuiFang = ('网页回放', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXStaticText[@AXValue='网页回放']")
Btn_Publish = ('课程发布btn', 'XPath', "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXSubrole='AXDialog']/AXButton[@AXTitle='发布']")
UnitItem = ('单元主题item', 'XPath', '(//div[@aria-describedby="rbd-hidden-text-0-hidden-text-0"])[last()]')
AddBtn = ('添加+', 'XPath', '(//div[@aria-describedby="rbd-hidden-text-0-hidden-text-0"][last()]/div/div/div/div/div/div/div/div[2]/div[2]/div)[1]')


# 课程下 搜索
SearchLogo = ('搜索 放大镜logo', 'XPaths', '(//img[@class="text-gray-400 auto-test-lms rounded"])[1]')
SearchText = ('搜索框', 'XPath', '//input[@placeholder="搜索学习活动"]')
SearchDel = ('清除搜索框内容X', 'XPath', '//div[@class="flex w-5 h-5 justify-center content-center cursor-pointer items-center auto-test-lms"]')


# 新建单元主题
UnitTopic = ('单元主题', 'XPath', '//div[text()="单元主题"]')
UnitTitle = ('单元主题主题', 'XPath', '//input[@placeholder="请填写单元主题名称(50字以内)"]')
UnitContent = ('单元主题内容', 'XPath', '//textarea[@placeholder="请填写单元介绍，包括学习目标、资源与建议等。"]')


# 新建录播课相关
Luboke = ('录播课', 'XPath', '//div[text()="录播课"]')
LubokeName = ('输入录播课名称', 'XPath', '//input[@placeholder="请填写录播课标题（50字以内）"]')
Choose_Yunpan = ('点击云盘选择', 'XPath', '//div[@title="从云盘选择"]')
File_Yunpan = ('选择云盘的视频', 'XPaths', '//i[@class="eeo-icon-uncheckbox"][1]')
LubokeEnsure = ('选择云盘的视频确定', 'XPath', '//span[text()="确定"]')


# 新建作业相关
Homework = ('作业', 'XPath', '//div[text()="作业"]')
HW_Name = ('输入作业名称', 'XPath', '//input[@placeholder="请填写作业标题（50字以内）"]')
HW_Content = ('输入作业内容', 'XPath', '//div[@aria-placeholder="请填写作业内容"]')


# 新建测验相关
Exam = ('测验', 'XPath', '//div[text()="测验"]')
ExamItem = ('全选本页', 'XPath', '//span[text()="全选本页"]')
ExamSet = ('组卷和设置', 'XPath', '//span[contains(text(),"下一步：组卷和设置")]')
ExamTitle = ('标题', 'XPath', '//input[@placeholder="请输入试卷标题（必填）"]')
ExamPublish = ('测验的发布btn', 'XPath', '//span[text()=" 发布 "]')    # //span[text()=" 发布 "]


# 新建讨论相关
Discuss = ('讨论', 'XPath', '//div[text()="讨论"]')
DisTitle = ('讨论标题', 'XPath', '//input[@placeholder="请填写讨论标题（50字以内）"]')
DisContent = ('讨论内容', 'XPath', '//div[@aria-placeholder="请填写讨论内容"]')


# 新建学习资料相关
Learning = ('学习资料', 'XPath', '//div[text()="学习资料"]')
LearningTitle = ('学习资料标题', 'XPath', '//input[@placeholder="请填写资料标题（50字以内）"]')
LearningContent = ('学习资料内容', 'XPath', '//div[@aria-placeholder="请填写资料内容"]')


# 复用其他班级课程
Copy = ('复用其他班级课程', 'XPath', '//span[text()= "复用其他班级课程"]')
CopyUnit = ('选择单元', 'XPath', '(//input[@class="ant-checkbox-input"])[1]')
CopyContinue = ('继续', 'XPath', '//button[@class="ant-btn ant-btn-primary false auto-test-lms"]')
CopySure = ('确定', 'XPath', '//span[text()="确定"]')


#  查看‘成绩’tab
StudyActivity = ('学习活动', 'XPath', '//div[text()="学习活动"]')
sut_list =('学生score列表的第一个人', 'XPath', '(//div[@class="flex items-center px-4 cursor-pointer"])[1]')


# 编辑相关公共元素
EditItem = ('活动搜索结果list，取最后一个进行编辑', 'XPath', '(//div[@class="truncate"])[last()]')
EditBtn = ('点击...里的编辑', 'XPath', '//span[text()="编辑"]')
EditEnsureNative = ('编辑确定btn-原生', 'Name', '确定')
EditEnsureH5 = ('编辑确定btn-web', 'XPath', '//button[@title="确定"]')  # 作业、讨论、录播课、学习资料(测验的另取其他)
"""
对活动详情页面添加标识的元素的说明：详情页面元素上添加了标识auto-test-lms
1. 添加标识的元素包括编辑入口'...'  和  页面关闭‘X’ 等。
2. 元素AutoTestLMS获取后是个list
作业--分享取数组下标0，编辑入口取数组下标1，页面关闭‘x’取数组下标2
课堂&测验&学习资料&讨论--编辑入口取数组下标0，页面关闭‘x’取数组下标1
录播课--编辑入口取数组下标0，页面关闭‘x’取数组下标1； 另有下标3和4定位在其他位置
学生成绩--页面关闭‘x’取数据下标0
测验编辑页面的【确定】--取数组下标0
"""
AutoTestLMS = ('各活动详情页面加标识的元素', 'XPaths', '//*[contains(@class, "auto-test-lms")]')


# 编辑 课堂 相关
EditAllowCheck = ('编辑-公开学习报告和评分', 'XPath', '//button[@id="isAllowCheck"]')


