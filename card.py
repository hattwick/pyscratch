# sample test from Fluent Python

import collections
from random import choice


Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

print(len(deck))
print('First card in the deck is',deck[0])
print('Last card in the deck is',deck[51])
print('Ramdom card is', choice(deck))

#print the full deck

print(deck[0:51])

for card in deck:
    print(card)