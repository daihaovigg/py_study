#!/usr/bin/python
#encoding:utf8

#define a class
class Student(object):

  def __init__(self,name,soc,age):
    self.name=name
    self.soc=soc
    self.__age=age  #private so you can't call it through a.__age or a.age

  def get_grade(self):
    if self.soc >= 90:
      return 'A'
    elif self.soc >= 60:
      return 'B'
    else :
      return 'C'

  def print_info(self):
    print self.name,self.soc,self.get_grade() #class.func call class.func


a=Student('dai',100,22)
a.weg=18  #this argument isn't in class but it also can be called in a
b=Student('li',59,23)
a.print_info()
print a.weg
b.print_info()

#inherit
class UT_STU(Student):
  def get_grade(self):  #覆盖父类的get_grade()方法
    if self.soc == 100:
      return 'S'
a = UT_STU('dai',100,22)
a.print_info()

print dir(a)

#add method to class
from types import MethodType
def set_soc(self,soc):
  self.soc=soc
a1=Student('dai',100,22)
a1.set_soc=MethodType(set_soc,a1,Student) #just add to a1
a1.set_soc(80)
a1.print_info()

Student.set_soc=MethodType(set_soc,None,Student)  #add to class
a2=Student('li',59,21)
a2.set_soc(61)
a2.print_info()


#property
class Stu(object):

  def __init__(self,name):
    self.__name=name

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self,name):
    self.__name=name

  def __str__(self):      #__str__()
    return 'Stu(object).name : %s' % self.name

a=Stu('dai')
print a.name
a.name='li'
print a.name
print a

#__iter__()
class Fib(object):
  def __init__(self):
    self.x,self.y=0,1
  def __iter__(self):
    return self      #call self

  def next(self):
    self.x,self.y=self.y,self.x+self.y
    if self.x>100 :
      raise StopIteration()
    return self.x

for a2 in Fib():
  print a2


#__getitem__()
#a class with slice : f[] or f[:]
class Fibc(object):
  def __getitem__(self,n):
    if isinstance(n,int):
      a,b=1,1
      for n in range(n):
        a,b=b,a+b
      return a
    elif isinstance(n,slice):
      a,b=1,1
      L=[]
      for x in range(n.stop):
        if x >= n.start :
          L.append(a)
        a,b=b,a+b
      return L

f= Fibc()
print f[0:5]


#call API bu URL
#creat a URL by __getattr__()
class Chain(object):
  def __init__(self,path=''):
    self._path=path
  def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))
  def __str__(self):
    return self._path

print Chain().status.usr.timeline.list

#with a argument
class Chain(object):
  def __init__(self,path=''):
    self._path=path
  def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))
  def __str__(self):
    return self._path
  def __call__(self,user):
    self._path+='/%s' % user
    return self
c=Chain()
print c.status.users('dai').repos

#type()
def fn(self,name):
  print 'haha %s' % name
Comi=type('Comi',(object,),dict(print_info=fn))
Comi().print_info('dai')

#metaclass
#pass this time
