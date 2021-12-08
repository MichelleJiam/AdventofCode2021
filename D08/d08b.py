#!/usr/bin/env python3

import difflib

def	findNum(code[], str, len):
	match len, len(difflib.ndiff(str, code[1])), 
		case 

sigList = []
outputList = []
with open('d08.in') as f:
	# sigList, outputList = [line.split('|') for line in f]
	for line in f:
		valList = line.split()
		delim = valList.index("|")
		sigList.append(valList[:delim])
		outputList.append(valList[delim + 1:])
# print(sigList)
# print(outputList)
# digits = [0] * 10
# len 2: 1
# len 3: 7
# len 4: 4
# len 5: 2, 3, 5
# len 6: 0, 6, 9
# len 7: 8
for sig in sigList:
	code = {}
	for s in sig:
		match len(s):
			case 2: code[1] = s
			case 3: code[7] = s
			case 4: code[4] = s
			case 7: code[8] = s
			case _: findNum(code, s, len(s))
		else:
			if l is 5:
				if len(difflib.ndiff(s, code[2]))
	

print(count)

