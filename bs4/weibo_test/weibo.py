#!/usr/bin/python
#-*-coding:utf8;-*-

import requests,os
import urllib,urllib2
from bs4 import BeautifulSoup
import cookielib,HTMLParser

cookies = cookielib.MozillaCookieJar('cookie.txt')
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = urllib2.Request(url,postdata,header=head)
def getHtml(url):
  Page = urllib2.urlopen(url)
  html = Page.read()
  return html
def getImg(html,path):
  soup=BeautifulSoup(html)
  x = 0
  for header in soup.find_all('img'):
    print header
    imgurl=header['src']
    #pat1=os.path.join(path,'%s.jpg' % x)
    print imgurl
    urllib.urlretrieve(imgurl,pat1)
    x += 1
html = getHtml('http://login.sina.com.cn/sso/login.php?client=ssologin.js')
print html
downpath=os.path.abspath('.')
downpath=os.path.join(downpath,'img')
#getImg(html,downpath)
