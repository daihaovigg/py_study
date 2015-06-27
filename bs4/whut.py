#!/usr/bin/python
#-*-coding:utf-8-*-

import urllib,urllib2,cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({'userName':'0121109310405','password':'daihao19931218','type':'xs','imageField.x':'62','imageField.y':'13'})
url='http://sso.jwc.whut.edu.cn/Certification/toLogin.do'
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers={'user-Agent':user_agent}
data = postdata
req = urllib2.Request(url,data,headers)
result = opener.open(req)
with open('whut.html','wb') as f:
  f.write(result.read())
