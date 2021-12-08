#!/usr/bin/env python3
from statistics import mean
from math import ceil, floor

with open('d07.in') as f:
	posList = [int(n) for n in f.read().split(",")]
avgHigh = ceil(mean(posList))
avgLow = floor(mean(posList))
growth = lambda x: x * (x + 1) / 2
fuelUseHigh = sum(growth(abs(p - avgHigh)) for p in posList)
fuelUseLow = sum(growth(abs(p - avgLow)) for p in posList)
print(min(fuelUseLow, fuelUseHigh))