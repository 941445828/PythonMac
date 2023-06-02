#### Mac端，LMS课程稳定性测试说明

##### 一、测试内容包括：
    1. LMS各活动
        新建：课堂、录播课、作业、测验、讨论、学习资料、单元主题
        操作：复用其他班级课程、查看学生成绩
        编辑：课堂、录播课、作业、测验、讨论、学习资料
            
##### 二、环境搭建:     
    
    【重要】：官方建议macOS版本在：10.7及以上
    
    1. python3.6
       如下，可下载python3.6.8
       https://www.python.org/ftp/python/3.6.8/python-3.6.8-macosx10.9.pkg
            
    2. 配置driver： AppiumForMac
       
       2.1. 从公共盘/Volumes/EEO（公共盘）/RD（产品研发中心）/RD-QA（测试组）/LMS  下获取driver到本地
       【注：请复制driver，不要删除或剪切走！！！】
[![p9sSGse.png](https://s1.ax1x.com/2023/05/11/p9sSGse.png)](https://imgse.com/i/p9sSGse)
       
       
       将放在本地的driver移动到应用程序Applications下
       
[![pSkhZIf.jpg](https://s1.ax1x.com/2023/01/05/pSkhZIf.jpg)](https://imgse.com/i/pSkhZIf)
         
        2.2. 打开系统设置--隐私与安全性--辅助功能--打开AppiumForMac
[![pSkhXlQ.png](https://s1.ax1x.com/2023/01/05/pSkhXlQ.png)](https://imgse.com/i/pSkhXlQ)

[![pSkhjyj.png](https://s1.ax1x.com/2023/01/05/pSkhjyj.png)](https://imgse.com/i/pSkhjyj)

[![pSkhzmn.png](https://s1.ax1x.com/2023/01/05/pSkhzmn.png)](https://imgse.com/i/pSkhzmn)

        2.2 运行脚本前，从Applications下点击打开将AppiumForMac（注：在桌面菜单栏中看到已打开即可，无界面）
        
        2.3 driver使用过程中若出现了如下提示：
[![pScXwLR.png](https://s1.ax1x.com/2023/02/06/pScXwLR.png)](https://imgse.com/i/pScXwLR)
        
        可在系统设置--隐私与安全性下，操作： 
[![pScXro6.png](https://s1.ax1x.com/2023/02/06/pScXro6.png)](https://imgse.com/i/pScXro6)

    3. 安装依赖  
       使用命令： pip3 install -r ./requirements.txt
       
    4. ClassIn版本设置
       从build下获取测试包，解压后，将app移动到Applications下
       
    
##### 三、【重要】运行脚本前，配置内容：

    1.1 配置文件，更新 ./config/stability_conf.py
            LOGIN_USER_NAME、LOGIN_PASS_WORD -- 登录用户名&密码
            CLASSNAME -- 功能运行所需班级(最好置顶，以防首屏找不到)，例如：新建的LMS活动都会放在这个班级下
            YUNPANFLODER -- 功能运行所需云盘下的文件夹，例如：上传视频文件需要，教室内打开课件需要
            CLASSFORCOPY -- 复用其他班级课程需要，最好置顶，以防首屏找不到；被复用的的单元下活动不要太多，以防被复制时超100个，失败
            online_loop -- int，功能循环使用次数
            files -- 云盘文件夹YUNPANFLODER下的课件列表
            
    1.2 其他前置配置需求
        确保所配置的班级CLASSNAME下，至少有两名学生存在(否则分组讨论功能不可用)
        云盘文件夹YUNPANFLODER，需要存在一个视频文件--.mp4、.3g2、.3gp等ClassIN支持的视频格式文件


##### 四、运行：
    1. 启动AppiumForMac
    
    2. 运行脚本：
       2.1 选择版本
            框架采用版本分离，在version目录下选择使用版本号
            例如，使用v5.0.0.0，使用目录V5000
            
       2.2 课程下，各活动操作：
            新建：课堂、录播课、作业、测验、讨论、学习资料、单元主题
            操作：复用其他班级课程、查看学生成绩
            编辑：课堂、录播课、作业、测验、讨论、学习资料
            运行脚本： version/v5000/run/stability/run_class_course.py
                 
       
##### 五、其他说明：
    1. 资料：https://github.com/appium/appium-for-mac