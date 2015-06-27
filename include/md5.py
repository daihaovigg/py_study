#!/usr/bin/python
#encoding:utf-8

import hashlib
from collections import defaultdict
db = defaultdict(lambda:'N/A')

def get_md5(password):
  md5 = hashlib.md5()
  md5.update(password)
  return md5.hexdigest()

def register(username,password):
  if db[username]!='N/A':
    print 'username has used!'
  else:
    db[username] = get_md5(password + username + 'the-Salt')
  return None

def login(username,password):
  if username in db:
    if db[username] == get_md5(password + username + 'the-Salt'):
      print 'loginSuccess!'
    else:
      print 'password is wrong!'
  else:
      print 'username is not exist!'
  return None

def loginmenu():
  while True:
    com=raw_input()
    if com=='r':
      u=raw_input('username:')
      p=raw_input('password:')
      register(u,p)
    elif com=='l':
      u=raw_input('username:')
      p=raw_input('password:')
      login(u,p)
    elif com=='q':
      break
  return None

if __name__ == '__main__':
  loginmenu()

