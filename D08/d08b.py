#!/usr/bin/env python3.10

# len of 2: 1
# len of 3: 7
# len of 4: 4
# len of 5: 2, 3, 5
# len of 6: 0, 6, 9
# len of 7: 8

def	findNum(sig, code):
	remSig = [s for s in (set(sig) - set(code))]
	for s in remSig:
		common_1 = [c for c in s if code[1].find(c) != -1]
		common_4 = [c for c in s if code[4].find(c) != -1]
		match len(s), len(common_1), len(common_4):
			case 5, 1, 2: code[2] = s
			case 5, 1, 3: code[5] = s
			case 5, 2, 3: code[3] = s
			case 6, 1, 3: code[6] = s
			case 6, 2, 3: code[0] = s
			case 6, _, _: code[9] = s

def findMasks(sig, code):
	for s in sig:
		match len(s):
			case 2: code[1] = s
			case 3: code[7] = s
			case 4: code[4] = s
			case 7: code[8] = s

with open('d08.in') as f:
	sigList, outputList = map(list, zip(*(line.split("|") for line in f)))
	outputList = [line.split() for line in outputList]
	sigList = [line.split() for line in sigList]

sumVal = 0
for i, sig in enumerate(sigList):
	code = ["" for x in range(10)]
	findMasks(sig, code)
	findNum(sig, code)
	val = [str(c_i) for o in outputList[i] for c_i, c in enumerate(code) if set(c) == set(o)]
	val = int("".join(val))
	sumVal += val
print(sumVal)