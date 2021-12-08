#!/usr/bin/env python

sigList = []
outputList = []
with open('d08.in') as f:
	for line in f:
		valList = line.split()
		delim = valList.index("|")
		sigList.append(valList[:delim])
		outputList.append(valList[delim + 1:])
# print(sigList)
# print(outputList)
# digits = [0] * 10
# digits = [digits[n] + 1 for n in 
count = 0
for val in outputList:
	for v in val:
		if len(v) in (2,3,4,7):
			print(v)
			count += 1 

print(count)

