#!/usr/bin/python
#-*- coding: utf-8 -*-  #保存为UTF-8，保证中文不乱码
b=abs(-5)
print b
a=abs  #用变量指向函数
b=a(-5)
print b
b=cmp(2,3)
print b

#自定义函数
def my_abs(x):
  if not isinstance (x,(int,float)):  #判断输入是否符合类型
    raise TypeError ('bad input type')  #不符合输出错误提示
  elif x>0 :
    print x
  else :
    print -x
def nop():
  pass #暂时不写语句

def my_swap(x,y):
  return y,x   #返回的是tuple

print my_swap(2,3)


#参数
#默认参数
def enroll(n,g,a=6,c='BJ'):
  print n,g,a,c

enroll('Bob','A',c='SH') #跳过默认参数a，直接赋值c


#可变参数
def calc(*numbers):
  sum1=0
  num=0
  for n in numbers:
    sum1=sum1+n*n
    num=num+1
  return sum1,num
print calc(1,2,3,4,5,6)

nums=[1,2,3,4]
print calc(*nums)


#关键字参数
def person(name,age,**kw):
  print name,age,kw
person('Dai',22,gender = 'M',job = 'IT')
daiinfo={'gender':'M','job':'IT'}
person('Dai',22,**daiinfo)

#参数组合
def mixfunc(a,b,c=0,*d,**e):
  print 'a=',a,'b=',b,'c=',c,'d=',d,'e=',e
mixfunc(1,2,(3,4),mos=99)
list1=(1,2,3,4)
dict3={'mos':99}
mixfunc(None,None,list1,dict3)


#递归

