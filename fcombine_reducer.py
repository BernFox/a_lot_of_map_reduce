#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

current = None
for item in reader:

	thisID = item[0]
	thisSection = item[1]

	if thisSection == "A":
		current = item

	if current and (thisID == current[0]) and (thisSection != current[1]):
		del item[1]
		item[0], item[3] = item[3], item[0]
		out =  item + current[2:]
		writer.writerow(out)
