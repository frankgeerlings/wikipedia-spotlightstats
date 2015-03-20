#!/usr/bin/env python

import json, httplib
from pprint import pprint

def stats(article):
	conn = httplib.HTTPConnection('stats.grok.se')
	conn.request("GET", "/json/nl/latest90/%s" % article)

	r = conn.getresponse()

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
	total = sum(figures) + biggest[1]
	print 'Biggest:', biggest
	print 'Mean: ', m
	print 'Std:  ', std(figures)
	print 'Popularity increase factor: ', biggest[1] / m
	print 'Number of standard deviations from the mean: ', (biggest[1] - m) / std(figures)
	print 'Total visits over last 90 days: ', total

if __name__ == "__main__":
	import sys

	args = sys.argv[1:]
	article = reduce(lambda x, y: x + ' ' + y, args, '')[1:].replace(' ', '_')
	pprint(article)
	stats(article)
