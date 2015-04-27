#!/usr/bin/python
#-*-coding:utf-8-*-

'test py running'   #explain and it can be called by hello.__doc__

__author__ = 'dai'

import sys

try :
  import cStringIO as StringIO  #尝试引入cStringIO,并指定别名StringIO引用
except ImportError:             #引入失败，捕获ImportError,重新引入StringIO
  import StringIO


#define private function
def _pri(name):
  print 'hello,%s' % name

#public will call the private
def mypri(name):
  _pri(name)

mypri('dai')

def test():
  args=sys.argv
  if len(args) == 1:
    print 'hello'
  elif len(args) == 2:
    print 'hello,%s' % args[1]
  else :
    print 'too many arguments'

if __name__ == '__main__':  #run this sigle
  test()
