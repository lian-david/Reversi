from cards import Card
import random

class DeckOfCards:
    """Represents deck of 52 playing cards
    """
    def __init__(self):
        s = ["Hearts", "Diamonds", "Clubs", "Spades"]
        f = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.deck = [Card(suit, face) for suit in s for face in f]

    def deal_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)

    def __str__(self):
        deck = " ".join(map(str, self.deck))
        return f'{deck}'

d = DeckOfCards()
print(d)
# d.deal_card()
# print(d)