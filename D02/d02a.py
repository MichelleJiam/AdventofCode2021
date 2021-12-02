#!/usr/bin/env python

with open('d02.in') as f:
	instList = [[type, int(val)] for type,val in [line.split() for line in f]]

pos = [0,0] # depth, horizontal pos

for type, val in instList:
	pos[0] += (type == "down") * val
	pos[0] -= (type == "up") * val
	pos[1] += (type == "forward") * val

print(pos[0] * pos[1])