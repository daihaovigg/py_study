#!/usr/bin/python
#encoding:utf-8
#logging
import logging
logging.basicConfig(level=logging.INFO)

import pdb

s='0'
n = int(s)
pdb.set_trace()
logging.info('n=%d' % n)
print 10 / n
