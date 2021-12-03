#!/usr/bin/env python
from collections import Counter

with open('d03.in') as f:
	binList = [line.strip() for line in f]
# print(binList[0:2])

gamma = ""
epsilon = ""
for i in range(len(binList[0])):
	col = [b[i] for b in binList]
	# print(col[0:5])
	counter = Counter(col).most_common(2)
	gamma += counter[0][0]
	epsilon += counter[1][0]
# gamma_b = ' '.join(format(ord(c), 'b') for c in gamma)
# gamma_b = bin(int(gamma, base=2))
gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)
print(gamma * epsilon)
