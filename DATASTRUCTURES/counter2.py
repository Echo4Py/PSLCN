#Version:Python2.7
from collections import *
import os

try:
    os.chdir(r'd:/pslcn')
    count_out = open('DATASTRUCTURES/countfile2', 'w+')
    with open(r'FILESYSTEM/filesystem', 'r') as f:
        data = f.read().decode('utf-8')
        count = Counter(data)
        for k in count.keys():
            #print k, ':', count[k]
            count_out.write(k.encode('utf-8'))
            count_out.write(':')
            count_out.write(str(count[k]))
            count_out.write('\n')
        
except IOError as werr:
    print('数据写入文件时发生错误' + str(werr))
finally:
    count_out.close()
    f.close()
