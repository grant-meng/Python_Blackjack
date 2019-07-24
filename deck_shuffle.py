import random
suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = []
shuffle_deck = []


def create_deck():
    for suit in suits:
        for card in cards:
            deck.append(f"{card} of {suit}")
    return deck


def shuffle():
    random.shuffle(deck)
    return deck



deck = create_deck()
shuffle()