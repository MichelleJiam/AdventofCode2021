#!/usr/bin/env python

with open('d08.in') as f:
	sigList, outputList = map(list, zip(*(line.split("|") for line in f)))
	outputList = [line.split() for line in outputList]

uniqueElems = [v for val in outputList for v in val if len(v) in (2,3,4,7)]
print(len(uniqueElems))