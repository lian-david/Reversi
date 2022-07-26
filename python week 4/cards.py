from abc import ABC

class Card(ABC):
    """Represents playing card and its attributes
    """
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face 

    def __str__(self):
        return f'Suit: {self.suit}, Face: {self.face}'