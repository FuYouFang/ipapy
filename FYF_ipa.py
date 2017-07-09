#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import optparse
import os
import sys
import getpass
import json
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import date, time, datetime, timedelta

# 配置文件夹
#commandPath = '/Users/' + getpass.getuser() + '/.ipa_build_py'
commandPath = '/Users/xuekai/.ipa_build_py'
# 配置文件名
# configFileName = "ipaBuildPyConfigFile.json"
# 配置文件路径
# configFilePath = os.path.join(commandPath, configFileName)




def initConfigFile():
    createConfigFile()
    initConfigFileContent()


    # 参数设置
def setOptparse():
    parser = optparse.OptionParser()
    # 参数配置指令
    parser.add_option('-c', '--config', action='store_true', default=None, help='config User''s dat')
    # 获取所有版本
    parser.add_option('-s', '--showTags', action='strore_true', default=None, help='show all tags')
    # 设置版本指令
    parser.add_option('-t', '--tag', default='master', help='app''s tag')
    options, arguments = parser.parse_args()
    global tag
    tag = options.tag
    # 配置信息
    if options.config == True and len(arguments) == 0:
        configMethod()
    # 获取所有版本
    if options.showTags == True and len(arguments) == 0:
        gitShowTags()

def configMethod():
    return

def gitShowTags():
    return

#主函数
def main():
    #设置配置文件路径
    initConfigFile()


main()