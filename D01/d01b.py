#!/usr/bin/env python
import operator

with open('d01.in') as f:
	array = []
	for line in f:
		array.append(int(line))

increases = 0
sums = []
for set in zip(array, array[1:], array[2:]):
	sums.append(sum(set))

for cur, nxt in zip(sums, sums[1:]):
	if cur < nxt:
		increases += 1

print(increases)