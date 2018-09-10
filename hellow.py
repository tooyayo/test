#!/usr/bin/python
# coding:utf-8

import re

text  = 'hello world'

strr = '(hell.)'
strrm = re.findall(strr,text)

print(strrm[0])