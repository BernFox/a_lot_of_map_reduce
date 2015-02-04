#!/usr/bin/python

import pandas as pd

data = open("file_results.txt")

data = data.readlines()
data = [line.strip().split("\t") for line in data]

results = {}

cols = ('page', 'total')

data1 = pd.DataFrame(data, columns=cols)
data1['total'] = data1['total'].apply(lambda x: float(x))