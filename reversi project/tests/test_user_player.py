from model.user_player import UserPlayer
import unittest

class TestUserPlayer(unittest.TestCase):
    def test_positive_input(self):
        result = UserPlayer.get_move("1, 8")
        self.assertAlmostEqual(result, 1, 8)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            UserPlayer.get_move("8")

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            UserPlayer.get_move("t, t")
        