#!/usr/bin/python
#-*-coding:utf8;-*-

import requests,os
import urllib,urllib2
from bs4 import BeautifulSoup

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0
def getHtml(url):
  Page = requests.session().get(url,headers=head,timeout=TimeOut)
  html = Page.content
  return html
def getImg(html,path):
  soup=BeautifulSoup(html)
  x = 0
  for header in soup.find_all('img',class_='BDE_Image'):
    #print header
    imgurl=header['src']
    pat1=os.path.join(path,'%s.jpg' % x)
    #print imgurl
    urllib.urlretrieve(imgurl,pat1)
    x += 1
html = getHtml('http://tieba.baidu.com/p/3771182693?lp=5028&mo_device=1&pn=0&')
#print html
downpath=os.path.abspath('.')
downpath=os.path.join(downpath,'img')
try:
  os.mkdir(downpath)
except:
  pass
getImg(html,downpath)
