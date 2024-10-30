# import necessary modules
import time
time.sleep(1)
import random

# defining ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# creating a deck
deck = [(rank, suit) for rank in ranks for suit in suits]

# shuffling the deck
random.shuffle(deck)

# spliting the deck
p1_deck = deck[:27]
p2_deck = deck[21:]

# comparing
def comp(p1_deck, p2_deck):
    if ranks.index(p1_deck[0]) == ranks.index(p2_deck[0]):
        return 0 # tie
    elif ranks.index(p1_deck[0]) > ranks.index(p2_deck[0]):
        return 1
    elif ranks.index(p1_deck[0]) < ranks.index(p2_deck[0]):
        return 2



def gameloop(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        end = comp(p1_card, p2_card)

        if end == 0: # tie
            peace(p1_deck, p2_deck, [p1_card, p2_card])
        elif end == 1: # p1 wins
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        elif end == 2: # p2 wins
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
    if len(p1_deck) > 0 and len(p2_deck) == 0:
        print("Player 1 wins")
    elif len(p1_deck) == 0 and len(p2_deck) > 0:
        print("Player 2 wins")
    elif len(p1_deck) == 0 and len(p2_deck) == 0:
        print("Tie!")

def peace(p1_deck, p2_deck, winner): # what happens when tie
    if len(p1_deck) < 4 or len(p2_deck) < 4: # not enough cards for the "war" exchange
        if len(p1_deck) > len(p2_deck):
            p2_deck = []
        elif len(p1_deck) < len(p2_deck):
            p1_deck = []
        else:
            p1_deck = []
            p2_deck = []
        return
    winner.extend(p1_deck.pop(0) for _ in range (3))
    winner.extend(p2_deck.pop(0) for _ in range (3))
    card_1 = p1_deck.pop(0)
    card_2 = p2_deck.pop(0)
    winner.append(card_1)
    winner.append(card_2)
    end = comp(card_1, card_2)
    if end == 1:
        p1_deck.extend(winner)
    elif end == 2:
        p2_deck.extend(winner)
    elif end == 0:
        peace(p1_deck, p2_deck, winning_deck)

gameloop(p1_deck, p2_deck)









