#!/usr/bin/python
# coding:utf-8

import re
from bs4 import BeautifulSoup

text  = 'hello world'

strr = '(hell.)'
strrm = re.findall(strr,text)

print(strrm[0])