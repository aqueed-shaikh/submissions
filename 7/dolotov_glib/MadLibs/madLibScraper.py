#!/usr/bin/env python

import requests
import os
import random

#access main mad-libs site
r = False
while not r:
    r = requests.get('http://www.elibs.com/')

#get urls of all mad libs puzzles
t = r.text
urls = []
i = t.count('<a href= "http://www.elibs.com/s')
while (i>0):
    t = t[t.find('<a href= "http://www.elibs.com/s'):]
    urls.append(t[t.find('http'):t.find('" ')])
    t = t[t.find('</a>'):]
    i -= 1

#selects random mad-lib from mad-lib "library"
i = random.randint(0,19)
url = urls.pop(i)
url2 = url[:url.find('Elibs') + 5] + 'Complete' + url[url.find('Elibs') + 5:]

#figures out what inputs are required. i.e. word types for the puzzle
r = False
while not r:
    r = requests.get(url)
    
t = r.text
usrin = []
i = t.count('value="%')
while (i>0):
    t = t[t.find('value="%'):]
    usrin.append(t[t.find('%')+1:t.find('%"')-1])
    t = t[t.find('/>'):]
    i -= 1

#my attempt to get the mad-lib puzzle text itself
r = False
while not r:
    r = requests.get(url2)

t = r.text
print(t)
