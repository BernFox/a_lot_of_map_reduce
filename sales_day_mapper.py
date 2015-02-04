#!/usr/bin/python

import sys
import datetime

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 6:
		continue

	date, time, store, item, cost, method = data
	date = [int(x) for x in date.split("-")]
	date = datetime.date(date[0], date[1], date[2])
	date = date.strftime("%A")
	sys.stdout.write("{0}\t{1}\n".format(date, cost))

            