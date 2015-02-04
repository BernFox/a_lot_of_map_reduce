#!/usr/bin/python

import sys
import csv
import re

word = "fantastically"

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#map(lambda x: writer.writerow(x), reader)
count = []
for item in reader:
	#print item
	body = re.findall(r"[\w']+", item[4])
	body = [x.lower() for x in body]
	if (len(item) == 19) and (word in body):			
		#count += body.count(word)
		#count.append(int(item[0]))
		#count += 1 
		if type(item[0]) != list:
			count.append(int(item[0]))
#count = sorted(count)
#print count[0]
print sorted(count)
		#writer.writerow(item)
	