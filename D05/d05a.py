#!/usr/bin/env python
import re
from collections import Counter

with open('test.in') as f:
	# line = [re.split(r'[,> c-]', line.strip()) for line in f]
	# ventList = [[int(num) for num in l if num is not ''] for l in line]
	ventList = [[int(num) for num in re.findall('\d+', line)] for line in f]
print(ventList)
# size = max(map(max, ventList)) + 1
size = 1000
ventMap = [[0] * size for i in range(size)]
linePoints = []
for x1, y1, x2, y2 in ventList:
	if x1 is x2 or y1 is y2:
		for col in range(min(x1, x2), max(x1, x2) + 1):
			for row in range(min(y1, y2), max(y1, y2) + 1):
				ventMap[row][col] += 1
				linePoints.append((col, row))

# for row in ventMap: print(row)
points = len([n for line in ventMap for n in line if n > 1])
print(points)

# count = Counter(linePoints)
# multiPoints = [coord for coord, freq in Counter(linePoints).items() if freq > 1]
# print(len(multiPoints))
