#!/usr/bin/env python3

import os
from os import listdir
from os.path import isfile, join
import datetime
import time

# 功能
# 1.一个 profile 的类，
# 1.一个 profileTool 的类，负责读取遍历所有的profile 文件，读取成 profile 的类，输出供其他类是使用

class Profile(object):
    name = None
    teamName = None
    UUID = None
    appIDName = None
    # applicationIdentifierPrefix = None
    applicationIdentifier = None
    creationDate = None


    def __init__(self, appIDName = None, applicationIdentifier = None, creationDate = None, name = None, teamName = None, UUID = None):
        self.appIDName = appIDName
        self.applicationIdentifier = applicationIdentifier
        self.creationDate = creationDate
        self.name = name
        self.teamName = teamName
        self.UUID = UUID

    def __str__(self):
        result = ''
        if self.name:
            result = 'name:%s' % self.name

        if self.teamName:
            result += 'teamName:%s' % self.teamName

        if self.UUID:
            result += ('UUID:%s' % self.UUID)

        if self.appIDName:
            result += ('appIDName:%s' % self.appIDName)

        if self.applicationIdentifier:
            result += ('applicationIdentifier:%s' % self.applicationIdentifier)

        if self.creationDate:
            result += ('createDate:%s' % self.creationDate)

        return result

# 问题 1：
# 在解析 profile 文件的时候，会使用下面的一行指令
# /usr/bin/security cms -D -i
# 不知道为什么，这个指令会输出下面的一句话，
# 不知道怎么清除它
# security: SecPolicySetValue: One or more parameters passed to a function were not valid.
#
# 问题 2：
# /usr/bin/security cms -D -i 输出的结果不知道怎么直接获取到 plist 结果，暂时先将内容输出到一个临时目录
#

class ProfileTool(object):
    # 存储 security 结果的临时目录
    profilePlistTempPath = os.path.expanduser('~/Documents/.fyfIpaTool')

    def __init__(self, profilePlistTempPath = None):
        if profilePlistTempPath:
            self.profilePlistTempPath = profilePlistTempPath
        self.initTempPath()

    def initTempPath(self):
        if not os.path.exists(self.profilePlistTempPath):
            try:
                os.makedirs(self.profilePlistTempPath)
            except OSError:
                print('create profilePlistTempPath:%s error', self.profilePlistTempPath)

    # 获取所有 profile 的信息
    def getTotalProfiles(self):
        profiles = {}
        # 获取所有的目录
        # profilePath = '~/Library/MobileDevice/Provisioning Profiles/'
        # profilePath = os.path.abspath('~/Library/MobileDevice/Provisioning Profiles/')
        # profilePath = os.path.join(os.path.expanduser('~'), 'Library/MobileDevice/Provisioning Profiles/')
        profileDocument = os.path.expanduser('~/Library/MobileDevice/Provisioning Profiles/')
        profileFileNames = [f for f in listdir(profileDocument) if isfile(join(profileDocument, f))]
        for profileFileName in profileFileNames:
            name, ext = os.path.splitext(profileFileName)
            if ext != '.mobileprovision':
                continue

            plistFileName = name + '.plist'
            profilePath = os.path.join(profileDocument, profileFileName)
            plistPath = os.path.join(self.profilePlistTempPath, plistFileName)
            print(profilePath)
            # 下面的指令会有一个下面的一行多余的输出
            # security: SecPolicySetValue: One or more parameters passed to a function were not valid.
            # os.system('/usr/bin/security cms -D -i "%s" -o %s > /dev/null' % (profilePath, plistPath))
            os.system('/usr/bin/security cms -D -i "%s" -o %s' % (profilePath, plistPath))

            profile = Profile()
            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :AppIDName" %s' % plistPath)
            for line in info:
                profile.appIDName = line.strip('\n')
                break

            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :Entitlements:application-identifier" %s' % plistPath)
            for line in info:
                profile.applicationIdentifier = line.strip('\n')
                break

            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :CreationDate" %s' % plistPath)
            for line in info:
                # 读取的字符串末尾有换行
                profile.creationDate = datetime.datetime.strptime(line.strip('\n'), '%a %b %d %H:%M:%S %Z %Y')
                break

            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :Name" %s' % plistPath)
            for line in info:
                profile.name = line.strip('\n')
                break

            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :TeamName" %s' % plistPath)
            for line in info:
                profile.teamName = line.strip('\n')
                break

            info = os.popen(r'/usr/libexec/PlistBuddy -c "Print :UUID" %s' % plistPath)
            for line in info:
                profile.UUID = line.strip('\n')
                break

            if profile.name and profile.name in profiles :
                preProfile = profiles[profile.name]
                if preProfile and profile.creationDate > preProfile.creationDate:
                    profiles[profile.name] = profile
            else:
                profiles[profile.name] = profile

        return list(profiles.values())

        # print(appIDName)

        # profileJson = os.popen('/usr/bin/security cms -D -i "%s"' % filePath)
        # print(profileJson)
        # print(os.system(
        #     r'/usr/libexec/PlistBuddy -c "Print :Entitlements:application-identifier" /dev/stdin <<< %s' % profileJson))

        # print('identifier:%s' % os.system('/usr/libexec/PlistBuddy -c "print :Entitlements:application-identifier) %s', profileJson))
        # print(os.system(
        #     r'/usr/libexec/PlistBuddy -c "Print :Entitlements:application-identifier" /dev/stdin <<< $(/usr/bin/security cms -D -i %s)' % filePath))
        # print(os.system(r'/usr/libexec/PlistBuddy -c "Print :" /dev/stdin <<< $(/usr/bin/security是 cms -D -i %s)' % filePath))
        # print(filePath)



if __name__ == '__main__':
    tool = ProfileTool()
    tool.getTotalProfile()
    # print(os.environ['HOME'])
    # print(os.path.expandvars('$HOME'))
    # print(os.path.expanduser('~'))

    # creationDate = datetime.datetime.strptime('Sat Jun 03 10:07:55 CST 2017', '%a %b %d %H:%M:%S %Z %Y')
    # print(creationDate)


