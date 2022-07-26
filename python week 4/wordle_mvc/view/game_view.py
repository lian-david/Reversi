from abc import ABC, abstractmethod

class GameView(ABC):
    def __init__(self, n_letters=5):
        self.n_letters = n_letters

    def display_welcome_message(self):
        pass

    def get_user_word(self):
        pass

    def display_match(self, user_word, match):
        pass

    def display_game_over(self, word_found, target_word):
        pass

