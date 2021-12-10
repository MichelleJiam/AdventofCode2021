#!/usr/bin/env python3

opener = "<{(["
closer = ">})]"
score = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('d10.in') as f:
	corrupted = []
	for line in f:
		line = [c for c in line if c != '\n']
		open_st = []
		for c in line:
			if c in opener:
				open_st.append(c)
			elif c in closer:
				if opener[closer.index(c)] == open_st[-1]:
					open_st.pop()
				else:
					corrupted.append(c)
					break
scores = [score[n] for n in corrupted]
print(sum(scores))
