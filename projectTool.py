#!/usr/bin/env python3


class projectTool(object):

    projectPath = None

    def __init__(self, projectPath):
        self.projectPath = projectPath

    def getInfoPlistWithTarget(self, target):
        return ''

if __name__ == '__main':
    projectPath = '/Users/xuekai/Documents/work/com/HappyFishing_iPhone_T'
    tool = projectTool(projectPath)

    infoPlistPath = tool.getInfoPlistWithTarget('HappyFishing_iPhone')
    print(infoPlistPath)