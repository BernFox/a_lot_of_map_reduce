#!/usr/bin/python

import sys

totalSales = 0
numSales = 0 
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	thisKey, thisValue = data	

	totalSales += float(thisValue)
	numSales += 1 

print "{0}\t{1}".format(totalSales, numSales)