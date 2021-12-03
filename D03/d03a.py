#!/usr/bin/env python
from collections import Counter

with open('d03.in') as f:
	binList = [line.strip() for line in f]

gamma = ""
epsilon = ""
for i in range(len(binList[0])):
	col = [b[i] for b in binList]
	counter = Counter(col).most_common(2)
	gamma += counter[0][0]
	epsilon += counter[1][0]
print(int(gamma, base=2) * int(epsilon, base=2))
