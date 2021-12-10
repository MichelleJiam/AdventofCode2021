#!/usr/bin/env python
import collections

def fishGrowth(popList, days):
	age_groups = [popList.count(str(i)) for i in range(9)]
	for d in range(days):
		age_groups = age_groups[1:] + [age_groups[0]] # shifting the array left 1
		age_groups[6] += age_groups[-1] # shifting the last element into 6th element
	return sum(age_groups)


with open('d06.in') as f:
	popList = f.read().split(",")
print(fishGrowth(popList, 80))