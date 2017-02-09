# -*- coding: utf-8 -*-

import urllib2

url = "http://news.yahoo.co.jp"
html = urllib2.urlopen(url)

#print(html.read())

#-----------------------------------------------

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

#print(soup.findAll())

#-----------------------------------------------
