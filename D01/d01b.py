#!/usr/bin/env python
import operator

with open('d01.in') as f:
	array = []
	for line in f:
		array.append([int(val) for val in line.split()])

increases = 0
sums = []

for a,b,c in zip(array, array[1:], array[2:]):
	s = (a+b+c)
	# print(s)
	sums.append(sum(s))

for cur, nxt in zip(sums, sums[1:]):
	# print(cur)
	if cur < nxt:
		increases += 1

print(increases)