#!/usr/bin/evn python3

import os
import json
import sys
import inspect

# commandPath = '.'
commandPath = '/Users/xuekai/.ipa_build_py'
# 配置文件名
configFileName = "ipaBuildPyConfigFile.json"
# 配置文件路径
configFilePath = os.path.join(commandPath, configFileName)

class ipaConfig(object):
    targetName = None
    gitPath = None
    certificateName = None
    firToken = None
    emailFromUser = None
    emailToUser = None
    emailPassword = None
    emailHost = None
    tempFinder = None
    mainPath = None
    keychainPassword = None

    def __init__(self):
        self.createConfigFile()

    def createConfigFile(self):
        if not os.path.exists(commandPath):
            try:
                os.makedirs(commandPath)
            except OSError:
                print('create commandPath error')

    # 初始化json配置文件
    def initConfigFileContent(self):
        return

        # outStr = json.dumps(js, ensure_ascii=False)
        # outStr
        # with open(configFilePath, 'w') as f:
        #     # f.write(outStr.strip().encode('utf-8') + '\n')
        #     # f.write(outStr.strip().encode('utf-8') + '\n'.encode('utf-8'))
        #     f.write(outStr.strip() + '\n')


# 另一种序列化的方法
# print(json.dumps(s, default=lambda obj: obj.__dict__))

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d
