#!/usr/bin/env python
from itertools import chain

def sumCard(card):
	sumC = sum([int(n) for n in card if n is not 'X'])
	return sumC


def	checkBingo(card, n):
	# horizontal check
	for row in zip(*[iter(card)]*5):
		if all(item=='X' for item in row):
			return True
		# [x]*n = a list of n amounts of x. [iter(s)*5] passes the same iterator 5 times to zip and zip dereferences that iterator each time.

	# vertical check
	for column in zip(card, card[5:], card[10:], card[15:], card[20:]):
		if all(item=='X' for item in column):
			return True

def crossCommon(cards, n):	
	for card in cards:
		if n in card:
			found = card.index(n)
			card[found] = 'X'
	return cards

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
			break;
	else: continue
	break
print(winners)
finalScore = sumCard(cards[winners[-1]]) * int(n)
print(finalScore)