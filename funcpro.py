#!/usr/bin/python
#-*-coding:utf-8-*-
#example high-order function
def add(x,y,f):
  return f(x)+f(y)
print add(-5,6,abs)

#Map/Reduce model
#change str into int
def str2int(s):
  def fn(x,y):
    return 10*x+y #caculate
  def char2num(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x] #change the char to int
  return reduce(fn,map(char2num,s))
print str2int('13241')

#standard English name
#way 1
def sta_name(L):
  return map(lambda x:x[0].upper()+x[1:].lower(),L)
print sta_name(['adam', 'LISA', 'barT'])
#way2
print map(lambda x:x.title(),['adam', 'LISA', 'barT'])

#filter()
def is_non(s):
  return s and s.strip()  #strip() delete the backspace from input
print filter(is_non,['sa',None,' ', 'da'])

#filter the prime number from 1~100
def is_pri(i):
  for a in range(2,i/2):
    if i%a == 0 :
      return True
  return False
print filter(is_pri,range(1,100))

#sort by sorted()
print sorted([3,7,5,8,1,9])

def o_cmp(x,y):
  if x>y:
    return -1
  elif x<y:
    return 1
  else :
    return 0
print sorted([3,7,5,8,1,9],o_cmp) #sort in inverted order

def ignore_case(x,y):
  x=x.lower()
  x=x.lower()
  if x>y:
    return 1
  elif x<y:
    return -1
  else :
    return 0
print sorted(['sa','ba','Daa','haha','HaHa'],ignore_case)   #steady sort ignore case


#return function
def lazy_sum(*args):
  def sum1():
    ax=0
    for n in args:
      ax=ax+n
    return ax
  return sum1
f=lazy_sum(1,3,5,7,9)
print f()

#closed hull
a=lambda:[lambda i=j:i*i for j in range(1,4)]
f1,f2,f3=a()
print f1(),f2(),f3()

#not closed hull,just a list creator
f1,f2,f3=[lambda i=j:i*i for j in range(1,4)]
print f1,f2,f3
print f1(),f2(),f3()

#test
a=lambda:(lambda i=0:i+1)
f1=a()
print f1()
f2=a()
print f2()

#decorator
import functools
def log(func):        #define a decorator
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print 'call %s()' % func.__name__     #attention : __name__ is make up of two _
    return func(*args,**kw)
  return wrapper

@log  #call log to decorate now()
def now():
  pass
print now()


#decorator with parameter
import functools
def log(text):        #define a decorator
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      print '%s %s()' % (text,func.__name__)     #attention : __name__ is make up of two _
      return func(*args,**kw)
    return wrapper
  return decorator

@log('call')
def now():
  pass
print now()

#exam
def log(func):        #define a decorator
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print 'begin call %s()' % func.__name__     #attention : __name__ is make up of two _
    return func(*args,**kw)
  print 'end call %s()' % func.__name__
  return wrapper
@log
def now():
  print 'calling'
print now()
