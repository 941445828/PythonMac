# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 登录 相关元素定位
"""

# 用户名
UserName = ("用户名", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='登录ClassIn' and @AXSubrole='AXDialog']/AXGroup[0]/AXGroup[0]/AXPopUpButton[0]")

# 密码
PassWord = ("密码", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='登录ClassIn' and @AXSubrole='AXDialog']/AXGroup[0]/AXGroup[0]/AXTextField[@AXSubrole='AXSecureTextField']")

# 登录
LoginButton = ("登录", "XPath", "/AXApplication[@AXTitle='ClassIn']/AXWindow[@AXTitle='登录ClassIn' and @AXSubrole='AXDialog']/AXGroup[0]/AXGroup[0]/AXButton[@AXTitle='登  录']")

