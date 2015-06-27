#!/usr/bin/python
#-*-coding:utf-8-*-

from PIL import Image,ImageDraw
import os,pdb

def ChangeImg(path,imgfile,x):
  img = Image.open(imgfile)
  #pdb.set_trace()
  w, h = img.size
  nimg=img.resize((320,240))
  path=os.path.join(path,'%s.jpg' % x)
  img.save(path,'jpeg')

def FindImg():
  path=os.path.abspath('.')
  imgfile = raw_input('Document:')
 # wid = raw_input('Width:')
 # hig = raw_input('High:')
  path = os.path.join(path,imgfile)
  n=0
  print path
  L=[x for x in os.listdir(path) if os.path.splitext(x)[1] == '.jpg']
  print L
  for imagelist in L:
    imagefile = os.path.join(path,imagelist)
    ChangeImg(path,imagefile,n)
    n=n+1

FindImg()
