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
from os import listdir
from os.path import isfile, join

import FYF_ipa_config


# 配置文件夹
#commandPath = '/Users/' + getpass.getuser() + '/.ipa_build_py'
commandPath = '/Users/xuekai/.fyf_ipa_build_py'
# 配置文件名
configFileName = "ipaBuildPyConfigFile.json"
# 配置文件路径
configFilePath = os.path.join(commandPath, configFileName)

# 初始化配置文件
def initConfigFile():
    # 初始化配置文件夹
    if not os.path.exists(commandPath):
        try:
            os.makedirs(commandPath)
            return True
        except OSError as error:
            print('创建配置文件夹失败：%s' % error)
            return False




def configMethod():
    return

def gitShowTags():
    return

# 1.判断是否存在帮助、展示类的参数
#   1.存在
#       1.展示帮助信息
#       2.展示其他参数
#
# 1.判断参数种是否存在 -c 或者 --config
#   1. 存在
#       1.判断本地是否保存有配置的 json
#           1.存在
#               1.检查本地的配置是否符合打包条件
#                   1.符合打包条件，输出本地配置，并开始用本地的配置进行打包
#                   2.不符合打包条件，
#                       1.输出不符合的条件，并提示进行确认，
#                       2.配置确认完成之后，对配置进行保存
#                       3.开始进行打包
#           2.不存在，逐条询问各个配置，询问完毕之后，进行打包
#
#   2. 不存在
#       1.逐条询问各个配置，
#       2.确定好配置后，保存配置
#       3.根据配置进行打包

class ipaTool(object):
    parser = optparse.OptionParser()
    options = None
    arguments = None
    config = None

    def __init__(self):
        self.setupParse();
        self.projectPath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T'

    # 参数设置
    def setupParse(self):
        # 参数配置指令
        self.parser.add_option('-c', '--config', action='store_true', default=None, help='config User''s dat')
        # 展示所有版本
        self.parser.add_option('-s', '--showTags', action='store_true', default=None, help='show all tags')
        # 设置版本指令
        self.parser.add_option('-t', '--tag', default='master', help='app''s tag')

        self.options, self.arguments = self.parser.parse_args();

    # 根据配置打包
    def packageWithConfig(self):
        self.cleanProgect()
        self.archiveProgect()
        self.exportArchive()

        #os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))

        return

    # 是否要根据配置打包
    def isPackageWithConfigInParser(self):
        return self.options.config == True

    # 是否要展示配置
    def isShowTagsInParser(self):
        return self.options.showTags == True

    # 展示 tags
    def showTagsInParser(self):
        print('展示tags')

    def checkConfig(self):
        return False

    # 判断是否是workspace
    def checkWorkSpace(self):
        if os.path.exists("%s/%s.xcworkspace" % (self.config.projectPath, self.config.targetName)):
            return True
        else:
            return False


    def compliteConfig(self):
        #taget = input('taget:')
        if self.config == None:
            self.config = FYF_ipa_config.IpaConfig()

        # 配置参数
        self.config.projectPath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T'
        self.config.targetName = 'HappyFishing_iPhone'
        self.config.archivePath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_archivePath/HappyFishing_iPhone.xcarchive'
        self.config.exportArchivePath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath'
        self.config.exportOptionsPlistFilePath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath/adhoc.plist'
        self.config.configuration = 'Release'
        # CODE_SIGN_IDENTITY = "iPhone Distribution: jianwei liu (F658SC654U)";
        self.config.identity = 'iPhone Distribution: jianwei liu (F658SC654U)'
        # PROVISIONING_PROFILE = "b2ec3855-d750-4e9c-a89a-3c8ced56c06d";
        # PROVISIONING_PROFILE_SPECIFIER = shangYuDistribution;
        self.config.profile = 'XC iOS Ad Hoc:com.xingyunld.shangyu'
        self.checkWorkSpace()

    def beginWork(self):
        if self.isShowTagsInParser():
            self.showTagsInParser()

        if self.isPackageWithConfigInParser():
            if not self.checkConfig():
                self.compliteConfig()
            self.packageWithConfig()


    # clean工程
    def cleanProgect(self):
        if self.checkWorkSpace():
            # xcodebuild clean -configuration "Release" -alltargets
            # os.system(
            #     'cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean' % (self.config.projectPath, self.config.targetName, self.config.targetName))
            print('cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean' % (self.config.projectPath, self.config.targetName, self.config.targetName))
        else:
            os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))
        return

    def archiveProgect(self):
        if self.checkWorkSpace():
            # os.system(
            #     'cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s -archivePath %s archive' % (self.config.projectPath, self.config.targetName, self.config.targetName, self.config.archivePath))
            print('cd %s;xcodebuild archive -workspace %s.xcworkspace -scheme %s -configuration %s -archivePath %s' % (
                self.config.projectPath,
                self.config.targetName,
                self.config.targetName,
                self.config.configuration,
                self.config.archivePath))
        else:
            os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))
        return

    # xcodebuild -exportArchive -archivePath /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_archivePath/HappyFishing_iPhone.xcarchive -exportPath /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath -exportOptionsPlist /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath/adhoc.plist CODE_SIGN_IDENTITY="iPhone Distribution: jianwei liu (F658SC654U)" PROVISIONING_PROFILE="b2ec3855-d750-4e9c-a89a-3c8ced56c06d"
    def exportArchive(self):
        if self.checkWorkSpace():
            # os.system(
            #     # 'cd %s;/'
            #     'xcodebuild -exportArchive /'
            #     '-archivePath %s  /'
            #     '-exportPath %s  /'
            #     '-exportOptionsPlist %s /'
            #     'CODE_SIGN_IDENTITY=%s /'
            #     'PROVISIONING_PROFILE=%s' % (
            #         # self.config.projectPath,
            #         self.config.archivePath,
            #         self.config.exportArchivePath,
            #         self.config.exportOptionsPlistFilePath,
            #         self.config.identity,
            #         self.config.profile
            #     ))

            print('cd %s; xcodebuild -exportArchive -archivePath %s  -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY=%s PROVISIONING_PROFILE=%s' % (
                    self.config.projectPath,
                    self.config.archivePath,
                    self.config.exportArchivePath,
                    self.config.exportOptionsPlistFilePath,
                    self.config.identity,
                    self.config.profile
                ))
        else:
            os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))
        return

    # Find an identity (certificate + private key)
    # 展示证书和秘钥
    # python调用Shell脚本或者是调用系统命令，
    # 有两种方法：os.system(cmd) 或os.popen(cmd),
    # 前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容。实际使用时视需求情况而选择。
    def showCodesigningIdentity(self):
        # os.system('security find-identity -p codesigning -v')
        result = os.pipe('security find-identity -p codesigning -v')
        test = result.read()
        print(test)

    def showTotalPorfile(self):
        profilePath = '/Users/xuekai/Documents/FYF/test/'
        profileFiles = [f for f in listdir(profilePath) if isfile(join(profilePath, f))]
        for profileFileName in profileFiles:
            filePath = os.path.join(profilePath, profileFileName)
            print(os.system(r'/usr/libexec/PlistBuddy -c "Print :Entitlements:application-identifier" /dev/stdin <<< $(/usr/bin/security cms -D -i %s)' % filePath))
            # print(os.system(r'/usr/libexec/PlistBuddy -c "Print :" /dev/stdin <<< $(/usr/bin/security cms -D -i %s)' % filePath))
            # print(filePath)

    def showPorgectProfile(self, bun):


#主函数
def main():
    #设置配置文件路径
    if initConfigFile():
        sys.exit(-1)

    tool = ipaTool()
    tool.beginWork()


if __name__ == '__main__':
    # main()
    tool = ipaTool()
    # tool.showCodesigningIdentity()
    tool.showTotalPorfile()