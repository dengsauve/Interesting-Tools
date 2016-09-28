from random import shuffle

class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]


class standard(object):
    def __init__(self):
        description = "Regular 52 Cards"
        suits = "hearts", "spades", "diamonds", "clubs"
        faces = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
        deck = []

        for suit in suits:
            for face in faces:
                deck.append(Card(suit, face))
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


    def living_large(self):
        deck, big_deck = self.deck, []
        for _ in range(6):
            for i in deck:
                big_deck.append(i)
        return big_deck


    def deal_hands(self):
        hand_one, hand_two = [], []
        for _ in range(2):
            hand_one.append(self.deck.pop(0))
            hand_two.append(self.deck.pop(0))
        return hand_one, hand_two


    def deal_another(self):
        return self.deck.pop(0)


class blackjack(standard):
    def __init__(self):
        description = "Large standard deck, 6 decks in one"
        standard.__init__(self)
        self.description = description
        self.deck = self.living_large()


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


def show_poker_hands(dealers_hand, players_hand):
    print("\n\n##############################")
    print("# Dealer Shows:", str(dealers_hand[0].rank), "of", str(dealers_hand[0].suit), "\n#")
    for i in range(len(players_hand)):
        print("# You Show:", str(players_hand[i].rank), "of", str(players_hand[i].suit))
    print("##############################")
    print("\n")


def get_points(hand):
    total = 0
    for i in range(len(hand)):
        total += hand[i].points
    if total > 21:
        for i in range(len(hand)):
            if hand[i].rank == "Ace" and total > 21:
                total -= 10
    return total


def print_options():
    print("""Options:
    1. Hit - Take another card.
    2. Stand - You're good.
    3. Fold - Too rich for my blood.""")
