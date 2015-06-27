#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2,re,urllib,os

def GetHtml(url):
  page = urllib2.urlopen(url)
  html = page.read()
  return html


def GetImage(html,path):
  reg = r'src="(.+?\.jpg)" pic_ext'
  imgre = re.compile(reg)
  imglist = re.findall(imgre,html)
  x=0
  for img in imglist:
    pat1=os.path.join(path,'%s.jpg' % x)
    urllib.urlretrieve(img,pat1)
    x=x+1
  return imglist

html = GetHtml('http://tieba.baidu.com/p/2460150866')
downpath=os.path.abspath('.')
downpath=os.path.join(downpath,'img')
os.mkdir(downpath)
GetImage(html,downpath)
