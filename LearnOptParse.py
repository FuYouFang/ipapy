from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i', '--input', action='store', dest='input', help='read input data from input file')
parser.add_option('-o', '--output', action='store', dest='output', help='write data to output file')
parser.add_option('-q', '--quite', action='store_false', dest='version', help='don\'t print the version')
# parser.add_option('-v', '--version', action='store_true', dest='version', default=False, help='print the version')
parser.add_option('-v', '--version', action='store_true', dest='version', help='print the version')

parser.add_option('-f', '--file', action='store', dest='file', help='file to handle')


#parser.add_option('-v', '--version', dest='version')

# 用一个数组模拟命令参数
testArgs = ['-i', 'someForInput', '-f', 'someForFile', '-vq']
options, args = parser.parse_args(testArgs)

print('options : %s' % options)
print('args : %s' % args)

if options.input :
    print('input in args : %s' % options.input)

if options.version :
    print('version 1.0.0')

print('version in args', options.version)

# 当 action 设置为 store_ture / store_false 时, 解析参数时, 如果有值 Ture / False, 没有的时候为 None
# 当 dest 相同时, 一个 action 设置为 store_false, 另一个 action 设置为 store_ture 时, 解析参数时,以后出现的为准
# 当 action 设置为 store 时, 解析参数时, 如果参数的数组只有 -f 而没有 -f 对应的参数是会报错