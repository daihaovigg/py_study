#!/usr/bin/python
#encoding:utf-8

try:
  print 'trying...'
  r = 10 / 0
  print 'result:',r
except ZeroDivisionError,e:
  print 'except:',e
finally:
  print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

#assert
# err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
  foo('0')
main()

