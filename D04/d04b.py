#!/usr/bin/env python
from itertools import chain
from d04a import checkBingo, crossCommon

with open('d04.in') as f:
	draws = [n.strip() for n in next(f).split(",")]
	next(f)
	cards = list(chain.from_iterable(line.split() for line in f))
cards = [cards[i:i+25] for i in range(0, len(cards), 25)]
winners = []
for n in draws:
	cards = crossCommon(cards, n)
	for i, card in enumerate(cards):
		if i not in winners and checkBingo(card, n):
			winners.append(i)
		if len(winners) is len(cards):
			break
	else: continue
	break
sumCard = sum([int(c) for c in cards[winners[-1]] if c is not 'X'])
print('Final score is: ', sumCard * int(n))