#!/usr/bin/python

import sys

totalSales = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	thisKey, thisValue = data	

	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, totalSales)
		oldKey = thisKey
		totalSales = 0

	oldKey = thisKey
	totalSales += float(thisValue)

if oldKey != None:
	print "{0}\t{1}".format(oldKey, totalSales)