#!/usr/bin/env python
#-*- coding: utf-8 -*-  #保存为UTF-8，保证中文不乱码
#代号
a=100

#:后跟缩进表示语句块
if a>0 :
  print '>'
else :
  print '<'



print r'''ad\'\'
...bd\"
...cd\t'''  #多行输出
print '中文测试'


#list有序可变列表
list1 = ['a','b','c']
print len(list1)
print list1[-1]
list1 = [1,2,3,['a','b']]
print list1 
print 'len=%d' % len(list1)
print list1[3]

#tuple有序不可变列表
tu=('a','b',list1)
print tu
print 'len=%d' % len(tu)

#判断
ifa=18
if a>18:
  print 'teen'
else:
  print 'child'

#循环
for i in ['dai','hao','ni','hao']:
  print i
sum1=0
for i in [1,2,3,4,5]:
  sum1 = sum1+i
  print sum1
sum2=0
for i in range(101):  #range(x)生成序列0到x
  sum2=sum2+i
print sum2

i=5
sum3=0
while i>0 :
  sum3=sum3+i
  i=i-1 #必须添加自减跳出循环
print sum3

#raw_input()类型转换
raw1 = raw_input('输入4与5进行判断：')
print raw1 > 5 
print ' 读入字符串4大于5成立'
raw1 = int(raw_input('输入4与5进行判断：'))
print raw1 > 5 
print ' 转换int型后4大于5不成立'


#dict
dict1 = {'a':1,'b':2,'c':3}
print dict1
print dict1['b']
print dict1.get('T',-1)
dict1.pop('c')
print dict1

#set
s1=set([1,1,2,2,3,3])
print s1
s1.add(4)
print s1
s1.remove(1)
print s1
s2=set([1,2,3,4,5])
print s1&s2
print s1|s2
