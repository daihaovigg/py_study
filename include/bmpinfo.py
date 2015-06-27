#!/usr/bin/python
#encoding:utf-8

import struct

path = raw_input('pls enter the entire path of the file: \n')

with open(path) as f:
	result = struct.unpack('<ccIIIIIIHH',f.read(30))    #<表示小端模式存储 
	if result[0]+result[1]=='BM' or result[0]+result[1]=='BA':
		print '位图大小： %s*%s ，位图颜色数%s' %(result[6],result[7],result[9])
	else :
		print 'not a bmp!'

