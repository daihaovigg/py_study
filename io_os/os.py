#!/usr/bin/python
#encodin:utf-8

import os
print os.name #os type
print os.uname()  #os infoemation in detail
print os.environ   #os environment
print os.getenv('PATH')  #get the need os environment

print [x for x in os.listdir('.') if os.path.isdir(x)]

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

def search(s,p='.'):
  for x in os.listdir(p):
    if os.path.isdir(x):
      search(s,os.path.join(p,x))
    elif s in x:
      print os.path.join(p,x)

search('test')
