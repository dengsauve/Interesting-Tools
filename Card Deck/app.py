#!/usr/bin/env python
# This is an expample / test of the card_deck library
from card_decks import standard, blackjack, show_poker_hands, get_points, print_options


def poker():
    deck = blackjack()
    deck.shuffle_deck()
    players_hand, dealers_hand = deck.deal_hands()
    playing, players_total = True, 0
    while playing and (players_total < 22):
        players_total = get_points(players_hand)
        show_poker_hands(dealers_hand, players_hand)
        print("You show a total of: %d and the dealer must beat 17." % players_total)
        print_options()
        choice = input("Your Move: ")
        if choice == "1": # Hit
            players_hand.append(deck.deal_another())
            players_total = get_points(players_hand)
        elif choice == "2": # Stand
            break
        elif choice == "3": # Fold
            playing = False
        else: # Invalid Choices
            print("An invalid choice, my friend. Please enter 1, 2, or 3.")

    if players_total > 21:
        print("BUSTED! You lose this round with %d points." % players_total)
    elif playing and players_total < 22:
        dealers_total = get_points(dealers_hand)
        while dealers_total < 17:
            dealers_hand.append(deck.deal_another())
            dealers_total = get_points(dealers_hand)
        if dealers_total > 21:
            print("Dealer Busts, You Win! Hooray!")
        elif dealers_total < 21 and dealers_total > players_total:
            print("Dealer shows %d, You Lose! So Sorry." % dealers_total)
        else:
            print("You show %d and dealer shows %d, You Win! Hooray!" % (players_total, dealers_total))
    else:
        print("That's right, walk away.")

def main():
    poker()

main()
