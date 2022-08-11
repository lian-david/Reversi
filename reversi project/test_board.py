from model.board import Board
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(8)

    def test_starting_positions(self):
        o1 = self.board._board[3][3]
        self.assertEqual(o1, 2)
        o2 = self.board._board[4][4]
        self.assertEqual(o2, 2)
        x1 = self.board._board[3][4]
        self.assertEqual(x1, 1)
        x2 = self.board._board[4][3] 
        self.assertEqual(x2, 1)

    def test_get_location(self):
        result = self.board.get_location(4, 5)
        self.assertEqual(result, self.board._board[4][5])

    def test_valid_location(self):
        result = self.board.valid_location(5, 6)
        self.assertEqual(result, True)

    def test_invalid_location(self):
        result = self.board.valid_location(9, 9)
        self.assertEqual(result, False)