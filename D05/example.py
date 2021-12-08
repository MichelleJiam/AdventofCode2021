#!/usr/bin/env python
from collections import Counter

ll = [x for x in open('d05.in').read().strip().split('\n')]

pts = []
for line in ll:
	x1=int(line.split()[0].split(",")[0])
	y1=int(line.split()[0].split(",")[1])

	x2=int(line.split()[2].split(",")[0])
	y2=int(line.split()[2].split(",")[1])
	if x1==x2 or y1==y2:
		for x in range(min(x1,x2),max(x1,x2)+1):
			for y in range(min(y1,y2),max(y1,y2)+1):
				pts.append((x,y))

print(len([x for (x,y) in Counter(pts).items() if y>1]))