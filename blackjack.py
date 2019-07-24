from deck_shuffle import shuffle
from get_value import get_value
from colorama import Fore
from time import sleep 
import itertools
import random
deck = shuffle()

def dealer_start(acecount):
    print(Fore.MAGENTA+"\nDealer's Cards: ")
    sleep(1)
    print("First Card: ", end='')
    acecount, card_value = get_card(acecount, deck)
    dealer_score = card_value
    sleep(1.5)
    print("Second Card: Hidded ")
    return dealer_score


def dealer_start2(acecount, dealer_score):
    print(Fore.MAGENTA+"\nDealer's Second Card: ", end='')
    acecount, card_value = get_card(acecount, deck)
    dealer_score += card_value
    dealer_score = check_ace(acecount, dealer_score)
    sleep(1)
    print(f"Total Score: {dealer_score}\n")
    sleep(1)
    dealer_score = dealer_hit(acecount, dealer_score)
    return dealer_score

    
def get_card(acecount, deck):
    card = deck[0]
    print(card)
    deck.pop(0)
    acecount, value = get_value(acecount, card)
    return acecount, value


def check_ace(acecount, dealer_score):
    if acecount > 0:
        if dealer_score > 21:
            dealer_score -= 10
            acecount -= 1
    return dealer_score


def dealer_hit(acecount, dealer_score):
    while True:
        if dealer_score <= 16:
            sleep(1)
            print(f"Draw Card: ", end='')
            acecount, draw = get_card(acecount, deck)
            dealer_score += draw
            dealer_score = check_ace(acecount, dealer_score)
            sleep(1)
            dealer_check_bust(dealer_score)
        else:
            sleep(1)
            print(f"Final Score: {dealer_score}")
            break
    return dealer_score


def again():
    again = input(Fore.WHITE+"\nWould you like to play again[Y/n]: ")
    if again == "N" or again == "n":
        print("Thank you for playing and goodbye!")
    else:
        start()

def hit(acecount, total_score):
    while True:
        sleep(1.5)
        hit = input(Fore.GREEN+"Would you like to hit?[Y/n]: ")
        if hit == "y" or hit == "Y":
            sleep(1)
            print(f"Draw Card: ", end='')
            acecount, draw = get_card(acecount, deck)
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

def dealer_check_bust(total_score):
    if total_score > 21:
        print(Fore.LIGHTGREEN_EX+"You Have Won Because The Dealer Busted!")
        again()




def visual(acecount):
    print(Fore.LIGHTBLUE_EX+"\nYour Cards: ")
    sleep(1)
    print("First Card: ", end='')
    acecount, card_value = get_card(acecount, deck)
    total_score = card_value
    sleep(1)
    print("Second Card: ", end='')
    acecount, card_value = get_card(acecount, deck)
    total_score += card_value
    sleep(1.5)
    print(f"Total Score: {total_score}\n")
    total_score = hit(acecount, total_score)
    return total_score


def start():
    acecount = 0
    while True:
        dealer_score = dealer_start(acecount)
        total_score = visual(acecount)
        dealer_score = dealer_start2(acecount, dealer_score)
        check_win(total_score, dealer_score)
        again = input(Fore.WHITE+"\nWould you like to play again[Y/n]: ")
        if again == "N" or again == "n":
            print("Thank you for playing and goodbye!")
            break
start()