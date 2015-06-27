#!/usr/bin/env python
#-*-coding:utf-8-*-
from urllib import urlopen
from bs4 import BeautifulSoup

url = 'http://movie.douban.com/'
text = urlopen(url).read()
soup = BeautifulSoup(text)

jobs = set()
for header in soup.find_all('li',class_ = 'ui-slide-item'):
  try :
    title = header['data-title']
    actors = header['data-actors']
    release = header['data-release']
    director = header['data-director']
    print ('%s-%s-%s-%s' % (title,release,director,actors))
  except KeyError:
    continue

