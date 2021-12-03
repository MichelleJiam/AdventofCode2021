#!/usr/bin/env python
from collections import Counter

def findLast()

with open('test.in') as f:
	binList = [line.strip() for line in f]

oxygen = binList
co2 = binList
for i in range(len(binList[0])):
	col = [b[i] for b in oxygen]
	counter = Counter(col).most_common(2)
	print(counter)
	if counter[0][1] == counter[1][1]:
		oxy_key = '1'
		co2_key = '0'
	else:
		oxy_key = counter[0][0]
		co2_key = counter[1][0]
	if (len(oxygen) > 1):
		oxygen = [n for n in oxygen if n[i] == oxy_key]
	if (len(co2) > 1):
		co2 = [n for n in co2 if n[i] == co2_key]
	print("i: ", i, " key: ", oxy_key, oxygen)
	print("key: ", co2_key, co2)
	print("\n")
	# if (len(oxygen) == 1 and len(co2) == 1):
	# 	print(i, ": found single match: ", oxygen, co2)
	# 	break;

oxygen = int(oxygen[0], base=2)
co2 = int(co2[0], base=2)
print(oxygen, co2)
print(oxygen * co2)
