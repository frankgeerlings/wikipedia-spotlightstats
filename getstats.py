#!/usr/bin/env python

import json, httplib
from pprint import pprint

conn = httplib.HTTPConnection('stats.grok.se')
conn.request("GET", "/json/nl/latest90/Geschiedenis_van_de_elektriciteit")

r = conn.getresponse()
print r.status, r.reason

body = r.read()

data = json.loads(body)

d = data['daily_views']

from operator import itemgetter

lis = [(x, d[x]) for x in d]
biggest = max(lis,key=itemgetter(1))
lis.remove(biggest)

from numpy import std, mean
figures = [x[1] for x in lis]

m = mean(figures)
print 'Biggest:', biggest
print 'Mean: ', m
print 'Std:  ', std(figures)
print 'Popularity increase factor: ', biggest[1] / m
print 'Number of standard deviations from the mean: ', (biggest[1] - m) / std(figures)
