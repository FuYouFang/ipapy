#!/usr/bin/env python3

import os
import getpass

# os模块 负责对文件的进行操作

# 1、os.path.exists(path) 判断一个目录是否存在
# 2、os.makedirs(path) 多层创建目录
# 3、os.mkdir(path) 创建目录

# file = '/Users/' + getpass.getuser() + '/Documents/pyTest/t1/t2/t3/t4'
# file = '/Users/xuekai/Documents/pyTest/t1/t2/t3/t4'
file1 = os.path.join('/Users/xuekai/Documents/', 'pyTest')
file2 = '/Users/xuekai/Documents/pyTest/t1/t2/t3/t4'

txt = os.path.join(file1, 'txt.txt')

# 如果想要创建的文件夹是已经存在的，那么执行上面的程序会出现下面的错误：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。

if not os.path.exists(file2):
    print('begin to mkdir')
    # os.mkdir(file2)
    os.makedirs(file2)

# try:
#     os.makedirs(file)
# except OSError:
#     print('创建目录失败')
# except:
#     print('未知错误,创建目录失败')

with open(txt, 'w') as f:
    print(f.write('hello world'))
