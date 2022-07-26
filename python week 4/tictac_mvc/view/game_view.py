from abc import ABC, abstractmethod
from model.game import Game

class GameView(ABC):
    def __init__(self, game):
        super().__init__()
        self.game = game

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass
    