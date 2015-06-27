#!/usr/bin/python
#-*-coding:utf-8-*-

import os,re,urllib,urllib2

url = 'http://movie.douban.com/'


def GetHtml(url):
  page = urllib2.urlopen(url)
  html = page.read()
  return html

def GetMovie(html):
  reg = r'class="ui-slide-item" (.*) data-intro'
  reg1 = r'title="(.*)" data-release'
  reg2 = r'release="(.*)" data-rate'
  reg3 = r'region="(.*)" data-director'
  reg4 = r'director="(.*)" data-actors'
  reg5 = r'actors="(.*)"'

  mvrelist = re.findall(reg,html)
  
  for mvin in mvrelist:
    mvstr="片名:"
    mvstr=mvstr+re.findall(reg1,mvin)[0]
    mvstr=mvstr+" 时期:"+re.findall(reg2,mvin)[0]
    mvstr=mvstr+" 地区:"+re.findall(reg3,mvin)[0]
    mvstr=mvstr+" 导演:"+re.findall(reg4,mvin)[0]
    mvstr=mvstr+" 主演:"+re.findall(reg5,mvin)[0]
    print mvstr

GetMovie(GetHtml(url))
