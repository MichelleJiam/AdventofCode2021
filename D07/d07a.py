#!/usr/bin/env python3
from statistics import median

with open('d07.in') as f:
	posList = [int(n) for n in f.read().split(",")]
mid = median(posList)
fuelUse = [abs(p-mid) for p in posList]
print(sum(fuelUse))