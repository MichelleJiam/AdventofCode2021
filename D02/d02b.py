#!/usr/bin/env python

with open('d02.in') as f:
	instList = [[type, int(val)] for type,val in [line.split() for line in f]]

aim = 0
pos = [0,0] # depth, horizontal pos

for type, val in instList:
	pos[0] += (type == "forward") * aim * val
	pos[1] += (type == "forward") * val
	aim += (type == "down") * val
	aim -= (type == "up") * val

print(pos[0] * pos[1])