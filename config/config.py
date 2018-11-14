# -*- coding:utf-8 -*-
"""
create_time:2018/11/12 11:19
file:config.py
@author:宁同刚
"""
import os
import platform

# 当前项目所在目录的绝对路径
parentDirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#页面元素信息路径
if platform.system()=="Windows":
    eleInfoPath=parentDirName+"\data\ele.yaml" #页面元素信息保存路径
    logPath=parentDirName+"\log\\" #日志保存路径
    phoneInfoPath=parentDirName+"\config\phoneInfo.Yaml" #手机及app配置信息地址
    casePath=parentDirName+"\data\case.xlsx"
else:
    eleInfoPath = parentDirName + "/data/ele.yaml"
    logPath = parentDirName + "/log/"  # 日志保存路径
    phoneInfoPath = parentDirName + "/config/phoneInfo.Yaml"
    casePath = parentDirName + "/data/case.xlsx"

WAIT_TIME=20


if __name__ == '__main__':
    print(parentDirName)
    print(platform.system())
