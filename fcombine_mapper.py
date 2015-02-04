#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for item in reader:
	if len(item) == 5:
		item.insert(1, "A")
		writer.writerow(item)
	elif len(item) == 19:
		#print len(item)
		del item[10:]
		del item[4]
		item.insert(1, "B")
		item[0], item[4] = item[4], item[0]
		writer.writerow(item)