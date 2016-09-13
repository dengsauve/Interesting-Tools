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
    print("Dealer Shows:", str(dealers_hand[0][1]), "of", str(dealers_hand[0][0]), "\n")
    for i in range(len(players_hand)):
        print("You Show:", str(players_hand[i][1]), "of", str(players_hand[i][0]))
    print("\n")


def get_points(hand):
    total = 0
    for i in range(len(hand)):
        if hand[i][1] == "11" or hand[i][1] == "12" or hand[i][1] == "13":
            total += 10
        else:
            total += int(hand[i][1])
    return total


def print_options():
    print("""Options:
    1. Hit - Take another card.
    2. Stand - You're good.
    3. Fold - Too rich for my blood.""")
