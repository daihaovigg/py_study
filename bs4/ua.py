#!/usr/bin/python
#-*-coding:utf-8-*-

import urllib,urllib2

url='http://www.baidu.com'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
value={'user-name' : '好d的htt'}
headers={'user-Agent':user_agent}
data = urllib.urlencode(value)
req = urllib2.Request(url,data,headers)
respon = urllib2.urlopen(req)
print respon.read()
