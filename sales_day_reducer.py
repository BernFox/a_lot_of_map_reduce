#!/usr/bin/python

import sys

totalSales = 0
oldKey = None
count = 0.0

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	thisKey, thisValue = data	

	if oldKey and oldKey != thisKey:
		mean = totalSales/count
		print "{0}\t{1}".format(oldKey, mean)
		oldKey = thisKey
		totalSales = 0
		count = 0

	oldKey = thisKey
	totalSales += float(thisValue)
	count += 1

if oldKey != None:
	mean = totalSales/count
	print "{0}\t{1}".format(oldKey, mean)