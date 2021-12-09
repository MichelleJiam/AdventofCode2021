#!/usr/bin/env python
import re

with open('d05.in') as f:
	ventList = [[int(num) for num in re.findall('\d+', line)] for line in f]
size = max(map(max, ventList)) + 1
ventMap = [[0] * size for i in range(size)]
for x1, y1, x2, y2 in ventList:
	if x1 == x2 or y1 == y2:
		for col in range(min(x1, x2), max(x1, x2) + 1):
			for row in range(min(y1, y2), max(y1, y2) + 1):
				ventMap[row][col] += 1

points = len([n for line in ventMap for n in line if n > 1])
print(points)