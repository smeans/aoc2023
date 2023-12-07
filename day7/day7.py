import sys
import re

from operator import attrgetter

raw = None
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    raw = f.read()

ad = raw.splitlines()

card_ranks = "23456789TJQKA"

def cards_to_val(cards):
    return [card_ranks.index(card) for card in cards]

def hand_rank(cards):
    cards = cards_to_val(cards)
    cc = [0] * len(card_ranks)
    for card in cards:
        cc[card] += 1

    cc.sort(reverse=True)

    fc = cc[:2]
    if fc == [5, 0]:
        return 6
    elif fc == [4, 1]:
        return 5
    elif fc == [3, 2]:
        return 4
    elif fc == [3, 1]:
        return 3
    elif fc == [2, 2]:
        return 2
    elif fc == [2, 1]:
        return 1

    return 0

hands = [{"cards": cards_to_val(a[0]), "hand_rank": hand_rank(a[0]), "bid": int(a[1])} for a in [line.split() for line in ad]]
hands = sorted(hands, key=lambda card: (card['hand_rank'], card['cards']))

total = sum([(i+1) * hand['bid'] for i, hand in enumerate(hands)])

print(hands)
print(f'total bids {total}')