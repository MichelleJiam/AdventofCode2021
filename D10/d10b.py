#!/usr/bin/env python3

from statistics import median

opener = "<{(["
closer = ">})]"
score = {')': 1, ']': 2, '}': 3, '>': 4}

with open('d10.in') as f:
	nav_list = [[c for c in line if c != '\n'] for line in f]

ac_score = []
for l, line in enumerate(nav_list):
	open_st = []
	for c in line:
		if c in opener:
			open_st.append(c)
		elif c in closer:
			if opener[closer.index(c)] == open_st[-1]:
				open_st.pop()
			else:
				open_st.clear()
				break
	if open_st:
		line_score = [score[closer[opener.index(o)]] for o in reversed(open_st)]
		linesum = 0
		for n in line_score:
			linesum = linesum * 5 + n
		ac_score.append(linesum)
print(median(sorted(ac_score)))