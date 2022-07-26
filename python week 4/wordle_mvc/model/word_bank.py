import random

class WordBank:
    """This class stores the list of words used for the game. 
    """
    def __init__(self, wordle_file):
        self.read_words_from_file(wordle_file)

    def read_words_from_file(self, wordle_file):
        with open(wordle_file) as f:
            self.words = [line[:-1] for line in f]

    def select_random_word(self):
        chosen_word = random.choice(self.words)
        return chosen_word

    def has_word(self, word):
        return word in self.words