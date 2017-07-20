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
from profileTool import ProfileTool
import re

# import profileTool

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
    configPath = os.path.expanduser('~/Documents/.fyfIpaTool')

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
        print('-------------- packageWithConfig ----------------')
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

    # 判断是否是workspace
    def checkWorkSpace(self):
        return True
        # if os.path.exists("%s/%s.xcworkspace" % (self.config.projectPath, self.config.targetName)):
        #     return True
        # else:
        #     return False

    # clean工程
    def cleanProgect(self):
        if self.checkWorkSpace():
            # xcodebuild clean -configuration "Release" -alltargets
            # os.system(
            #     'cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean' % (self.config.projectPath, self.config.targetName, self.config.targetName))
            print('cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean' % (
                self.config.projectPath, self.config.targetName, self.config.targetName))
        else:
            os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))
        return


    def beginWork(self):
        if self.isShowTagsInParser():
            self.showTagsInParser()

        if self.isPackageWithConfigInParser():
            if not self.checkConfig():
                self.compliteConfig()
            self.packageWithConfig()


    # -----------------------------------------
    #    开始配置相关参数
    # -----------------------------------------

    # 检查配置的参数是否符合要求
    def checkConfig(self):
        return False

    # 配置参数
    def compliteConfig(self):
        #taget = input('taget:')
        if self.config == None:
            self.config = FYF_ipa_config.IpaConfig()

        #
        self.setConfigProjectPath()
        self.setConfigTargetName()
        self.setConfigArchivePath()
        self.setConfigExportArchivePath()
        self.setConfigIdentity()
        self.setConfigPorfile()
        self.setConfigConfiguration()
        self.setConfigCompileBitcode()
        self.setConfigExportMethod()
        self.setConfigExportOptionsPlistFilePath()
        # 配置参数
        self.checkWorkSpace()

    def setConfigExportArchivePath(self):
        path = input('请输入导出地址：')
        # 示例
        # '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath'
        self.config.exportArchivePath = path

    def setConfigProjectPath(self):
        path = input('请输入项目地址：')
        # 示例
        # '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T'
        self.config.projectPath = path

    def setConfigTargetName(self):
        targetName = input('请输入 targetName：')
        # 示例
        # 'HappyFishing_iPhone'
        self.config.targetName = targetName

    def setConfigArchivePath(self):
        archivePath = input('请输入 archivePath:')
        # 示例
        # '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_archivePath/HappyFishing_iPhone.xcarchive'
        self.config.archivePath = os.path.join(archivePath.strip(' '), ('%s.xcarchive' % self.config.targetName))

    # Find an identity (certificate + private key)
    # 展示证书和秘钥
    # python调用Shell脚本或者是调用系统命令，
    # 有两种方法：os.system(cmd) 或os.popen(cmd),
    # 前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容。实际使用时视需求情况而选择。
    def setConfigIdentity(self):
        # os.system('security find-identity -p codesigning -v')
        identitys = []
        result = os.popen('security find-identity -p codesigning -v')
        print('----------------- 所有的 证书 -----------------')
        for line in result:
            # 示例：
            # '1) FD819672C289A675C5A0EA0B92BABDBEDC95396B "iPhone Developer: Keli Hu (82YGMCAFJC)"'
            r = re.search(r'"(.*)"', line)
            if r :
                print(line)
                identitys.append(r.group(1))

        index = -1
        while True:
            index = input('请选择 证书 的序号：')
            index = int(index)
            if (index >= 0 and index < len(identitys)):
                break

        identity = identitys[index]
        print('选择 证书 为：%s' % (identity))

        # 示例
        # CODE_SIGN_IDENTITY = "iPhone Distribution: jianwei liu (F658SC654U)";
        # self.config.identity = 'iPhone Distribution: jianwei liu (F658SC654U)'
        self.config.identity = identity

    # 展示所有 profile
    def setConfigPorfile(self):
        profileTool = ProfileTool(self.configPath)
        profiles = profileTool.getTotalProfiles()

        print(type(profiles))
        print('----------------- 所有的 profile -----------------')
        for index, profile in enumerate(profiles):
            print('%s.%s - %s - %s' % (index, profile.name, profile.applicationIdentifier, profile.UUID))

        index = -1
        while True:
            index = input('请选择 profile 的序号：')
            index = int(index)
            if (index >= 0 and index < len(profiles)):
                break

        profile = profiles[index]
        print('选择 profile 为：%s - %s' % (profile.name, profile.UUID))

        # 示例：
        # PROVISIONING_PROFILE = "b2ec3855-d750-4e9c-a89a-3c8ced56c06d";
        # PROVISIONING_PROFILE_SPECIFIER = shangYuDistribution;
        # self.config.profile = 'XC iOS Ad Hoc:com.xingyunld.shangyu'
        self.config.profile = profile.UUID

    def setConfigConfiguration(self):
        print('----------------- 模式 -----------------')
        print('0. Debug')
        print('1. Release')

        index = -1
        while True:
            index = input('请选择 模式 的序号：')
            index = int(index)
            if (index >= 0 and index < 2):
                break
        if index == 1:
            self.config.configuration = 'Release'
        else:
            self.config.configuration = 'Debug'

    def setConfigCompileBitcode(self):
        print('----------------- Bitcode -----------------')
        print('0. No')
        print('1. Yes')
        index = -1
        while True:
            index = input('请选择 Bitcode 的序号：')
            index = int(index)
            if (index >= 0 and index < 2):
                break
        if index == 1:
            self.config.compileBitcode = True
        else:
            self.config.compileBitcode = False

    def setConfigExportMethod(self):
        print('----------------- ExportMethod -----------------')
        print('0. app-store')
        print('1. ad-hoc')
        print('2. enterprise')
        print('3. development')
        index = -1
        while True:
            index = input('请选择 Bitcode 的序号：')
            index = int(index)
            if (index >= 0 and index < 4):
                break

        if index == 0:
            self.config.exportMethod = 'app-store'
        elif index == 1:
           self.config.exportMethod = 'ad-hoc'
        elif index == 2:
            self.config.exportMethod = 'enterprise'
        elif index == 3:
            self.config.exportMethod = 'development'

    def setConfigExportOptionsPlistFilePath(self):
        optionsPlistFilePath = os.path.join(self.configPath, 'ExportOptions.plist')
        print('optionsPlistFilePath:%s' % optionsPlistFilePath)

        # with open(optionsPlistFilePath, 'w') as f:
        #     f.write(r'<?xml version="1.0" encoding="UTF-8"?>\n')
        #     f.write(r'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
        #     f.write(r'<plist version="1.0">\n')
        #     f.write(r'<dict>\n')
        #     f.write(r'<key>compileBitcode</key>\n')
        #     if self.config.compileBitcode:
        #         f.write(r'<ture/>\n')
        #     else:
        #         f.write(r'<false/>\n')
        #     f.write(r'<key>method</key>\n')
        #     f.write(r'<string>%s</string>\n' % self.config.exportMethod)
        #     f.write(r'</dict>\n')
        #     f.write(r'</plist>\n')
        lines = []
        lines.append(r'<?xml version="1.0" encoding="UTF-8"?>')
        lines.append(r'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
        lines.append(r'<plist version="1.0">')
        lines.append(r'<dict>')
        lines.append(r'<key>compileBitcode</key>')
        if self.config.compileBitcode:
            lines.append(r'<ture/>')
        else:
            lines.append(r'<false/>')
        lines.append(r'<key>method</key>')
        lines.append(r'<string>%s</string>' % self.config.exportMethod)
        lines.append(r'</dict>')
        lines.append(r'</plist>')

        with open(optionsPlistFilePath, 'w') as f:
            f.writelines(lines)

        # 示例
        # '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath/adhoc.plist'
        self.config.exportOptionsPlistFilePath = optionsPlistFilePath


    # -----------------------------------------
    #
    # -----------------------------------------
    def archiveProgect(self):
        print('------------------- archiveProgect ----------------------')
        if self.checkWorkSpace():
            print('cd %s;xcodebuild archive -workspace %s.xcworkspace -scheme %s -configuration %s -archivePath %s' % (
                self.config.projectPath,
                self.config.targetName,
                self.config.targetName,
                self.config.configuration,
                self.config.archivePath))

            os.system(
                'cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s -archivePath %s archive' % (self.config.projectPath, self.config.targetName, self.config.targetName, self.config.archivePath))

        else:
            os.system('cd %s;xcodebuild -target %s clean' % (self.config.projectPath, self.config.targetName))
        return

    # -----------------------------------------
    #
    # -----------------------------------------
    # xcodebuild -exportArchive -archivePath /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_archivePath/HappyFishing_iPhone.xcarchive -exportPath /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath -exportOptionsPlist /Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath/adhoc.plist CODE_SIGN_IDENTITY="iPhone Distribution: jianwei liu (F658SC654U)" PROVISIONING_PROFILE="b2ec3855-d750-4e9c-a89a-3c8ced56c06d"
    def exportArchive(self):
        print('------------------- exportArchive ----------------------')
        if self.checkWorkSpace():
            print('cd %s; xcodebuild -exportArchive -archivePath %s  -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' % (
                    self.config.projectPath,
                    self.config.archivePath,
                    self.config.exportArchivePath,
                    self.config.exportOptionsPlistFilePath,
                    self.config.identity,
                    self.config.profile
                ))
            os.system('cd %s; xcodebuild -exportArchive -archivePath %s  -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' % (
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



#主函数
def main():
    #设置配置文件路径
    if initConfigFile():
        sys.exit(-1)

    tool = ipaTool()
    tool.beginWork()


# 正则表达式
if __name__ == '__main__':
    main()

    # os.system(
    #     'cd %s; xcodebuild -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' % (
    #         '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T',
    #         '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_archivePath/HappyFishing_iPhone.xcarchive',
    #         '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T_exportArchivePath',
    #         '/Users/xuekai/Documents/.fyfIpaTool/ExportOptions.plist',
    #         'iPhone Developer: jianwei liu (5N4G2447Z5)',
    #         'f79e6cc2-0076-43f0-a0b2-63545c9d0953'
    #     ))

    # tool = ipaTool()
    # tool.setConfigIdentity()
    #tool.setConfigPorfile()
    # test = '1) FD819672C289A675C5A0EA0B92BABDBEDC95396B "iPhone Developer: Keli Hu (82YGMCAFJC)"'
    # test = '"d"s'
    # result = re.search(r'"(.*)"', test)
    # print(result.group(0))

    # lines = []
    # lines.append(r'<?xml version="1.0" encoding="UTF-8"?>')
    # lines.append(
    #     r'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
    # lines.append(r'<plist version="1.0">')
    # lines.append(r'<dict>')
    # lines.append(r'<key>compileBitcode</key>')
    #
    # lines.append(r'<false/>')
    # lines.append(r'<key>method</key>')
    # lines.append(r'<string>ad-Hoc</string>')
    # lines.append(r'</dict>')
    # lines.append(r'</plist>')
    #
    # with open('/Users/xuekai/Documents/.fyfIpaTool/ExportOptions.plist', 'w') as f:
    #     f.writelines(lines)


