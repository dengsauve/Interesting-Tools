from random import shuffle

class standard(object):
    def __init__(self):
        description = "Regular 52 Cards"
        suits = "hearts", "spades", "diamonds", "clubs"
        faces = tuple(range(1,13))
        deck = []

        for suit in suits:
            for face in faces:
                deck.append([suit, face])

        self.description = description
        self.suits = suits
        self.faces = faces
        self.deck = deck

    def __repr__(self):
        return '<card_deck> %r' % self.description

    def __str__(self):
        rs = []
        for card in self.deck:
            rs.append(card[0] + " " + str(card[1]))
        return ",\n".join(rs)

    def shuffle_deck(self):
        shuffle(self.deck)


class blackjack(standard):
    def __init__(self):
        description = "Large standard deck, 6 decks in one"
        standard.__init__(self)
        self.description = description
        self.deck = living_large(self.deck)

    def living_large(deck):
        big_deck = []
        for _ in range(6):
            big_deck = big_deck + deck
        return big_deck


class pinochle(standard):
    def __init__(self, name):
        description = "Pinochle Deck. 48 Cards."
        suits = standard.suits
        faces = 1, 9, 10, 11, 12, 13
        deck = []
        for suit in suits:
            for face in faces:
                deck.append([suit, face])
                deck.append([suit, face])

        standard.__init__(self, name)
        self.description = description
        self.faces = faces
