#!/usr/bin/env python
#-*-coding:utf-8-*-

html_doc= """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://weibo.com/276145500/home?wvr=5" class="sister" id="link1">Elsie</a>,
<a href="http://weibo.com/276145500/home?wvr=5" class="sister" id="link2">Lacie</a> and
<a href="http://weibo.com/276145500/home?wvr=5" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc)
with open('alice.html','wb') as f:
  f.write(soup.prettify())


