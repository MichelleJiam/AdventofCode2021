#!/usr/bin/env python

with open('d01.in') as f:
	array = []
	for line in f:
		array.append(int(line))

increases = 0
for cur, nxt in zip(array, array[1:]):
	if cur < nxt:
		increases += 1

print(increases)