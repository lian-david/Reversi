from model.ai_player import AI
from model.reversi_game import ReversiGame
from model.board import Board
import unittest

class TestSimpleAI(unittest.TestCase):
    def setUp(self):
        self.game = ReversiGame(8)
        self.AI = AI(self.game)

    def test_board_attribute(self):
        self.assertIsInstance(self.AI.board, Board)

    def test_get_move_error(self):
        with self.assertRaises(UnboundLocalError):
            self.AI.get_move()
