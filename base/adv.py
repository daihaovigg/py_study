#!/usr/bin/python
#-*-coding:utf-8-*-
#切片
L=range(100)
print L[::5],'\n',L[-5:-1],'\n',L[-10::2]
S='abcdefg'
print S[:4:2]

#迭代
tr1='abcdefg'  #字符串迭代
for i in tr1:
  print i

dict1={'a':1,'b':2,'c':3}
for k in dict1:  #默认迭代key
  print k
for v in dict1.itervalues():  #迭代value
  print v
for k,v in dict1.iteritems(): #迭代key and value
  print k,v


from collections import Iterable  #import Iterable pack
print isinstance('avs',Iterable)  #judge if can iteration
print isinstance(123,Iterable)  #judge the integer

#enumerate()索引元素对
for k,v in enumerate(['A','B','C']):
  print k,v

for x,y in [(1,2),(6,7),(9,0)]:
  print x,y

#列表生成器
print [x*x for x in range(1,11)]  #range(x,y) == [x,x+1,...,y-1]
print [x*x for x in range(1,11) if x%2 ==0]  #add if judge 
print [m+n for m in 'ABC' for n in 'XYZ'] #double circle

import os
print [d for d in os.listdir('.')]  #list all files in the document

L=['Hello','World',18,'Dai']
#chang High lable in lower except others
print [s.lower() for s in L if isinstance(s,str)] #will return ERROR without 'if' beacuse there isn't a lower() in a list which isn't a str
#change but with output others
print [s.lower() if isinstance(s,str) else s for s in L]

#生成器generator
g=(x*x for x in range(10))  #define generator
for i in range(10):
  print g.next()  #call generator by next()
m=(x*x for x in range(10))  #define a new generator because the old is next to the tial so it couldn't iterate again
for i in m:
  print i       #call generator by iterate

#define a fibonacci generator_func
def fib(max):
  a,b,n=0,1,0
  while n<max:
    yield b
    a,b=b,a+b
    n=n+1
a=fib(10)  #call fib generator_func to creat a new genrator
for i in a:
  print i #iterate
