#!/usr/bin/env python
from collections import Counter

def findLast(list, tiebreaker, i):
	if i == len(list[0]) or len(list) == 1:
		return list
	col = [entry[i] for entry in list]
	counter = Counter(col).most_common(2)
	if counter[0][1] == counter[1][1]:
		key = tiebreaker
	else:
		key = counter[(tiebreaker != '1')][0]
	list = [n for n in list if n[i] == key]
	return findLast(list, tiebreaker, i + 1)


with open('d03.in') as f:
	binList = [line.strip() for line in f]
oxygen = findLast(binList, '1', 0)
co2 = findLast(binList, '0', 0)
print(int(oxygen[0], base=2) * int(co2[0], base=2))
