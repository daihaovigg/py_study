#!/usr/bin/env python
# -*- coding: utf-8 -*-
monkey = [0] * 50
monkey[0] = 1
monkey[1] = 2
for i in xrange(48):
      monkey[i+2] = monkey[i] + monkey[i+1]
print monkey[49]


def feb(x):
  a,b,n=0,1,0
  while n<x:
    a,b=b,a+b
    n=n+1
  return b
x=int(raw_input())
print feb(x)
