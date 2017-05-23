# Card class
# Spades   = 3
# Hearts   = 2
# Diamonds = 1
# Clubs    = 0

# Jack       = 11
# Queen      = 12
# King       = 13

import random

class Card(object):
    """ Represents a playing card """
    def __init__(self, suit = 0, rank =2):
        self.suit = suit
        self.rank = rank

    # card attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        #compare suits
        if self.suit > other.suit: return  1
        if self.suit < other.suit: return -1
        #compare ranks
        if self.rank > other.rank: return  1
        if self.rank < other.rank: return -1
        # same rank, same suit, tie
        return 0
    #more defs required:
    #__eq__ ==
    #__ne__ !=
    #__le__ <=
    #__gt__ >=


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res = [] #empty list
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

kod = Card(1, 13)
qod = Card(1,12)
print(kod, ' and ', qod)

newDeck = Deck()

#for i in range(1,len(newDeck.cards)):
#    print(newDeck.cards[i])

for card in newDeck.cards:
    print(card)

print(newDeck) # MUCH quicker because it's printing one string once.

    
