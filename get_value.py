def get_value(acecount, card):
    if "Ace" in card:
        card_value = 11
        acecount += 1
    elif "2" in card:
        card_value = 2
    elif  "3" in card:
        card_value = 3
    elif "4" in card:
        card_value = 4
    elif "5" in card:
        card_value = 5
    elif "6" in card:
        card_value = 6
    elif "7" in card:
        card_value = 7
    elif "8" in card:
        card_value = 8
    elif "9" in card:
        card_value = 9
    elif "10" in card:
        card_value = 10
    elif "Jack" in card:
        card_value = 10
    elif "Queen" in card:
        card_value = 10
    elif "King" in card:
        card_value = 10
    return acecount, card_value
