#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")


	if len(data) != 2:
		continue

	path, value = data
	#if "?" in str(path):
	#	path = str(path)[:path.find("?")]

	if 'http://www.the-associates.co.uk' in path:
		path = path.replace('http://www.the-associates.co.uk','')

	if 'http://the-associates.co.uk' in path:
		path = path.replace('http://the-associates.co.uk','')

	if 'https://www.the-associates.co.uk' in path:
		path = path.replace('https://www.the-associates.co.uk','')

	if 'https://the-associates.co.uk' in path:
		path = path.replace('https://the-associates.co.uk','')
	
	print "{0}\t{1}".format(path, value)

