#!/usr/bin/env python
# This is an expample / test of the card_deck library

from card_decks import standard

kem_cards = standard()
print kem_cards

kem_cards.shuffle_deck()

print kem_cards
