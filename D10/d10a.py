#!/usr/bin/env python3

import pyparsing as pp


def isPair(c1, c2):
	if c1 == "(" and c2 == ")":
		return True
	elif c1 == "[" and c2 == "]":
		return True
	elif c1 == "{" and c2 == "}":
		return True
	elif c1 == "<" and c2 == ">":
		return True
	return False

with open('test.in') as f:
	for line in f:
		line = [c for c in line if c != '\n']
		# pairs = 0
		# print(line)
		# for c in range(len(line)):
		# 	if c < len(line) - 1:
		# 		if not isPair(line[c], line[c+1]):
		# 			continue
		# 		else:
		# 			pairs += 1
		# 			print(c, ": ", line[c], line[c+1])
		# 			line.pop(c)
		# 			line.pop(c+1)
		# 			print(line)
		# print("pairs: ", pairs, " len: ", len(line))
		break
opener  = pp.Regex(r'[<{([]') 
closer = pp.Regex(r'[>})\]]')
pattern = opener + pp.FollowedBy(closer)
attr_expr = pp.Group(pattern + pp.OneOrMore(opener, stopOn=pattern))
line = "[({(<(())[]>[[{[]{<()<>>"
# val = pp.OneOrMore(opener).parseString(line)
val = pp.OneOrMore(attr_expr).parseString(line)
print(val.dump())
