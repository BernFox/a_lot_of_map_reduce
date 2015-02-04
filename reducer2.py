#!/usr/bin/python

import sys

oldKey = None
maxSale = 0

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	thisKey, thisValue = data		

	if oldKey and (oldKey != thisKey):
		print "{0}\t{1}".format(oldKey, maxSale)
		oldKey = thisKey
		maxSale = 0

	oldKey = thisKey
	if float(thisValue) > float(maxSale):
		maxSale = float(thisValue)

if oldKey != None:
	print "{0}\t{1}".format(oldKey, maxSale)