#!/usr/bin/env python
from d06a import fishGrowth

with open('d06.in') as f:
	popList = f.read().split(",")
print(fishGrowth(popList, 256))