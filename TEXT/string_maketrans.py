# coding=utf-8
import string
dict = string.maketrans('abcdefghijklmnopqrstuvwy', '123$%^789!@#456&*(0)`~-_')
dictcn = string.maketrans('我不知道天空中还有些什么能让我们看到美好的事情', '你说的话要经过真理的检验最终就可以判断出是否对')

s = raw_input()
"""
with open('string') as f:
    s = f.read()
    print '中文加密是这样的：'+'\n'+s.translate(dictcn)
    f.close()
"""
print '你输入的内容是：'+s
print '内容经过加密是：'+s.translate(dict)
