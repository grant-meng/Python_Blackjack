from deck_shuffle import shuffle
import dealer_blackjack as dbj
from get_value import get_value
from colorama import Fore
from time import sleep
import itertools
import random
deck = shuffle()


def get_card(deck):
    card = deck[0]
    print(card)
    deck.pop(0)
    acecount, card_value = get_value(card)
    return acecount, card_value


def check_ace(acecount, total_score):
    if acecount > 0:
        if total_score > 21:
            total_score -= 10
            acecount -= 1
    return total_score

def again():
    again = input(Fore.WHITE+"\nWould you like to play again[Y/n]: ")
    if again == "N" or again == "n":
        print("Thank you for playing and goodbye!")
    else:
        start()

def hit(total_score):
    while True:
        sleep(1.5)
        hit = input(Fore.GREEN+"Would you like to hit?[Y/n]: ")
        if hit == "y" or hit == "Y":
            sleep(1)
            print(f"Draw Card: ", end='')
            acecount, draw = get_card(deck)
            total_score += draw
            total_score = check_ace(acecount, total_score)
            sleep(1)
            check_bust(total_score)
            print(f"Total Score: {total_score}\n")
        else:
            sleep(1)
            print(f"Final Score: {total_score}")
            break
    return total_score


def check_win(total_score, dealer_score):
    if total_score > dealer_score:
        print(Fore.LIGHTMAGENTA_EX+"\nCongrats You Beat The Dealer!")
    elif dealer_score > total_score:
        print(Fore.RED+"\nYou Lost To The Dealer!")
    else:
        print(Fore.YELLOW+"\nYou And The Dealer Tied!")


def check_bust(total_score):
    if total_score > 21:
        print("You Have Lost By Busting!")
        again()


def visual():
    print(Fore.LIGHTBLUE_EX+"\nYour Cards: ")
    sleep(1)
    print("First Card: ", end='')
    acecount, card_value = get_card(deck)
    total_score = card_value
    sleep(1)
    print("Second Card: ", end='')
    acecount, card_value = get_card(deck)
    total_score += card_value
    sleep(1.5)
    print(f"Total Score: {total_score}\n")
    total_score = hit(total_score)
    return total_score


def start():
    while True:
        dealer_score = dbj.dealer_start()
        total_score = visual()
        dealer_score = dbj.dealer_start2(dealer_score)
        check_win(total_score, dealer_score)
        again = input(Fore.WHITE+"\nWould you like to play again[Y/n]: ")
        if again == "N" or again == "n":
            print("Thank you for playing and goodbye!")
            break
        elif again == "Y" or again == "y":
            continue
        else: 
            break

start()