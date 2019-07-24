from deck_shuffle import shuffle
from get_value import get_value
from time import sleep
import itertools
import random
from colorama import Fore
deck = shuffle()


def get_card(deck):
    card = deck[0]
    print(card)
    deck.pop(0)
    acecount, value = get_value(card)
    return acecount, value


def check_ace(acecount, dealer_score):
    if acecount > 0:
        if dealer_score > 21:
            dealer_score -= 10
            acecount -= 1
    return dealer_score


def check_bust(total_score):
    if total_score > 21:
        print(Fore.LIGHTGREEN_EX+"You Have Won Because The Dealer Busted!")
        exit()


def hit(dealer_score):
    while True:
        if dealer_score <= 16:
            sleep(1)
            print(f"Draw Card: ", end='')
            acecount, draw = get_card(deck)
            dealer_score += draw
            dealer_score = check_ace(acecount, dealer_score)
            sleep(1)
            check_bust(dealer_score)
        else:
            sleep(1)
            print(f"Final Score: {dealer_score}")
            break
    return dealer_score


def dealer_start():
    print(Fore.MAGENTA+"\nDealer's Cards: ")
    sleep(1)
    print("First Card: ", end='')
    acecount, card_value = get_card(deck)
    dealer_score = card_value
    sleep(1.5)
    print("Second Card: Hidded ")
    return dealer_score


def dealer_start2(dealer_score):
    print(Fore.MAGENTA+"\nDealer's Second Card: ", end='')
    acecount, card_value = get_card(deck)
    dealer_score += card_value
    dealer_score = check_ace(acecount, dealer_score)
    sleep(1)
    print(f"Total Score: {dealer_score}\n")
    sleep(1)
    dealer_score = hit(dealer_score)
    return dealer_score