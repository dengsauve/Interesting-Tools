#!/usr/bin/env python
# This is an expample / test of the card_deck library
from card_decks import standard, blackjack, show_poker_hands, get_points


def poker():
    deck = blackjack()
    deck.shuffle_deck()
    players_hand, dealers_hand = deck.deal_hands()
    # print(dealers_hand, players_hand)
    playing = True
    players_total = 0
    while playing and (players_total < 22):
        players_total = get_points(players_hand)
        show_poker_hands(dealers_hand, players_hand)
        print("You show a total of: %d and the dealer must beat 17." % players_total)
        print("""Options:
        1. Hit - Take another card.
        2. Stand - You're good.
        3. Fold - Too rich for my blood.""")
        choice = input("Your Move: ")
        if choice == "1":
            players_hand.append(deck.deal_another())
            players_total = get_points(players_hand)
        elif choice == "2":
            break
        elif choice == "3":
            print("sissy pants")
            playing = False
        else:
            print("You've broken the rules. A man can get shot for that in Vegas.")
            playing = False

    if players_total > 21:
        print("BUSTED! You lose this round.")
    elif playing and players_total < 22:
        print("Dealer Magic")
    else:
        print("That's right, walk away.")

def main():
    poker()

main()
