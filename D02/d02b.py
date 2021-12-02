#!/usr/bin/env python

def instructionType(instruction):
	if instruction.find("forward") != -1:
		return (0, 1)
	elif instruction.find("down") != -1:
		return (1, 0)
	elif instruction.find("up") != -1:
		return (-1, 0)
	else:
		return (0, 0)

with open('d02.in') as f:
	instr = []
	for line in f:
		instruction = line.split()
		type = instructionType(instruction[0])
		instr.append([type, int(instruction[1])])
aim = 0
pos = [0,0] # depth, horizontal pos
for instruction in instr:
	if (instruction[0][0] == 0):
		pos[0] += aim * instruction[1]
	pos[1] += instruction[0][1] * instruction[1]
	aim += instruction[0][0] * instruction[1]
print(pos[0] * pos[1])