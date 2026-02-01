
import random

while True:
    print("Choose:")
    print("1 - Rock ✊")
    print("2 - Paper ✋")
    print("3 - Scissors ✌️")
    print("0 - Exit")

# choose suit
suit_number = random.randint(1, 4)

if suit_number == 1:
    suit = "♥"
elif suit_number == 2:
    suit = "♦"
elif suit_number == 3:
    suit = "♣"
else:
    suit = "♠"

# choose card value
card_number = random.randint(1, 13)

if card_number == 1:
    card = "A"
elif card_number == 11:
    card = "J"
elif card_number == 12:
    card = "Q"
elif card_number == 13:
    card = "K"
else:
    card = card_number

print("Your card is:", card, suit)
