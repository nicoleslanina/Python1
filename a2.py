# import necessary modules
import random

# defining ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# creating a deck
deck = [(rank, suit) for rank in ranks for suit in suits]

# shuffling the deck
random.shuffle(deck)

# spliting the deck
player1_deck = deck[:27]
player2_deck = deck[21:]

# comparing
card_comp(player1_deck.pop(0), player2_deck.pop(0))

