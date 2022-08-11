from model.ai_minimax import AdvancedAI
from model.reversi_game import ReversiGame
from model.board import Board
import unittest

class TestAdvancedAI(unittest.TestCase):
    def setUp(self):
        self.game = ReversiGame(8)
        self.AI = AdvancedAI(self.game)

    def test_board_attribute(self):
        self.assertIsInstance(self.AI.board, Board)

    def test_get_move_error(self):
        with self.assertRaises(UnboundLocalError):
            self.AI.get_move()