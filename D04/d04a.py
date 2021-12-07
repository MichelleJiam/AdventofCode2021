#!/usr/bin/env python
from itertools import chain

def	checkBingo(card, n):
	for row in zip(*[iter(card)]*5):	# horizontal check
		if all(item=='X' for item in row):
			return True
		# [x]*n = a list of n amounts of x. [iter(s)*5] passes the same iterator 5 times to zip and zip dereferences that iterator each time.

	# for column in zip(card[::5]): #works with grabbing column but doesn't work for all() comparison
	for column in zip(card, card[5:], card[10:], card[15:], card[20:]):	# vertical check
		if all(item=='X' for item in column):
			return True

def crossCommon(cards, n):
	for card in cards:
		if n in card:
			card[card.index(n)] = 'X'
	return cards

if __name__ == "__main__":
	with open('test.in') as f:
		draws = [n.strip() for n in next(f).split(",")]
		next(f)
		cards = list(chain.from_iterable(line.split() for line in f))
	cards = [cards[i:i+25] for i in range(0, len(cards), 25)]

	for n in draws:
		cards = crossCommon(cards, n)
		for card in cards:
			if checkBingo(card, n):
				# print('Bingo at number ', n)
				sumC = sum([int(c) for c in card if c is not 'X'])
				print('Final score is: ', sumC * int(n))
				break
		else: continue
		break