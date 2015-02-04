#!/usr/bin/python

import sys

totalHits = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	data[0] = data[0].strip()

	if len(data) != 2:
		continue

	thisKey, thisValue = data	
	thisValue = float(thisValues)

	if oldKey == thisKey[:-1]:
		thisKey = thisKey[:-1]

	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, totalHits)
		oldKey = thisKey
		totalHits = 0

	oldKey = thisKey
	totalHits += float(thisValue)

#if oldKey != None:
#	print "{0}\t{1}".format(oldKey, totalHits)