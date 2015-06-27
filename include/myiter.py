#!/usr/bin/python
#encoding:utf-8

import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n
for c in itertools.chain('ABC', 'XYZ'):
    print c

for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group) # 为什么这里要用list()函数呢？

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group) # 为什么这里要用list()函数呢？

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
