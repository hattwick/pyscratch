import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
deck = FrenchDeck()



print(deck[0:51])
print('Total Cards: ',len(deck))

# orderly print

print('/// Starting Deck Print///')
count = 0
for card in reversed(deck):
    print(card)
    count = count + 1
    #  reverse = True
print('/// End of Deck.  ',count,' cards printed///')

print('Sort by suit and value')

suit_values = dict(spaces=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


#End - stopping point
