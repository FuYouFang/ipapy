#!/usr/bin/env python3

import getpass

# 获取当前登录的用户名。
user = getpass.getuser()
print('current user is : %s' % user)

# 获取输入的密码，并且输入内容屏幕不显示，和Linux系统登录类似
password = getpass.getpass('input your password:')

print('your input password is : %s' % password)