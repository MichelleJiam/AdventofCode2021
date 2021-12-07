#!/usr/bin/env python
from itertools import chain
import operator

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
	# for column in zip(card[::5]): #works with grabbing column but doesn't work for all() comparison
	for column in zip(card, card[5:], card[10:], card[15:], card[20:]):
		if all(item=='X' for item in column):
			return True

def crossCommon(cards, n):
	# ind_dict = dict((k,i) for i,k in enumerate(card))
	# inter = set(ind_dict).intersection(draws)
	# indices = [ind_dict[x] for x in inter]
	# print(indices) #doesn't work, prints random indices?

	# set_card = set(card)
	# for n in draws:
	# 	if n in set_card:

	# for n in draws:
	# 	if n in card:
	# 		found = card.index(n)
	# 		card[found] = 'X'
			# print('found ', n, ' at ', found) # works but need to check for bingo with each draw
	
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

	# while True:
	# 	card = list(islice(f, 1, 6))
	# 	if not card: break
	# 	cards.append([row.split() for row in card])

for n in draws:
	cards = crossCommon(cards, n)
	for card in cards:
		if checkBingo(card, n):
			print('Bingo at number ', n)
			sumC = sumCard(card)
			finalScore = sumC * int(n)
			print(sumC, '*', n, finalScore)
			break
	else: continue
	break

# for card in cards:
# 	# card = map(crossCommon, card)
# 	card = crossCommon(card, draws)
# 	intersect = [i for i in card if i in draws]
# print(intersect)
# print(draws)
# print(cards)