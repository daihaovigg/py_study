#!/usr/bin/python
#-*-coding:utf8;-*-

import requests,os
import urllib,urllib2
from bs4 import BeautifulSoup
import re,sys
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0

downpath=os.path.abspath('.')
downpath=os.path.join(downpath,'img')
try:
  os.mkdir(downpath)
except:
  pass

def rph(a, b, c):           #建立显示进度的reporthook函数  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    sys.stdout.write( '文件大小：%s byte     下载进度：%.2f%% \r' %(c,per))

def getHtml(url):
  Page = requests.session().get(url,headers=head,timeout=TimeOut)
  html = Page.content
  return html
def getImg(html,path,num):
  soup=BeautifulSoup(html)
  for header in soup.find_all('img',id=re.compile("{.*}")):
    imgurl=header['src']
    pat1=os.path.join(path,'%s.jpg' % num)
    urllib.urlretrieve(imgurl,pat1,rph)
html = 'http://www.sd.xinhuanet.com/news/yule/2015-05/30/c_1115450775'
req=getHtml(html+'.htm')
x=0
getImg(req,downpath,x)
x=x+1
for y in range(2,8):
  content='_%s' % y
  htm2=html+content    #join会把_加到开头
  htm2=htm2+'.htm'
  req=getHtml(htm2)
  getImg(req,downpath,x)
  x=x+1
