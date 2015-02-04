#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")

	if len(data) != 10:
		continue

	IP, identity, username, date, zone, method, path, protocol, status, size = data
	if "?" in str(path):
		path = str(path)[:path.find("?")]
	print "{0}\t{1}".format(IP, 1)

