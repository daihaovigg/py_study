#!/usr/bin/python
#encoding:utf8


import codecs
with codecs.open('a.txt','w','gbk') as f:
  f.write(u'\u6d4b\u8bd5')  #以gbk的模式写入了unicode的中文‘测试’


import json
d=dict(name='dai',age=22,scor=100)
with open('b.txt','wb') as f:
  json.dump(d,f)

