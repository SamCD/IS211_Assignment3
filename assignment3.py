#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3"""

import csv
import urllib2
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--url')
args = parser.parse_args()

req = urllib2.Request(args.url)
dldata = urllib2.urlopen(req)
history = csv.reader(dldata)
hits = 0.0
total = 0.0
browsers = {'Firefox':[r'\b(Firefox)\W',r'\b(Seamonkey)\W',0],
            'Chrome': [r'\b(Chrome)\W',r'\b(Chromium)\W',0],
            'IE': [r'\b(MSIE)\b',r'fhasldkfjhsaldkfjha',0],
            'Safari': [r'\b(Safari)\W',r'\b(Chrome|Chromium)\W',0]
            }

for item in history:
    if re.search(r'(GIF|gif|JPG|jpg|PNG|png|JPEG|jpeg)$',item[0]):
        hits += 1
    total += 1
    for key,val in browsers.iteritems():
        if re.search(val[0],item[2]) and not re.search(val[1],item[2]):
            val[2] += 1
print 'Image requests account for {}% of all requests'.format(

                                                        hits * 100 / total)
topval = 0
topbrows = ''
for key, value in browsers.iteritems():
    if value[2] > topval:
        topval = value[2]
        topbrows = key

print 'The most used browser is {} with {} hits'.format(topbrows, topval)
