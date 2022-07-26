from view.game_view import GameView
from model.letter_type import LetterType

class GameConsoleView(GameView):
    symbols = {
        LetterType.CORRECT_PLACE: "*",
        LetterType.CORRECT_LETTER: "+",
        LetterType.INCORRECT_LETTER: "-"
    }

    def __init__(self, n_letters=5):
        super().__init__(n_letters)

    def display_welcome_message(self):
        print("Welcome to Wordle")
        print("-------------------")

    def get_user_word(self):
        user_word = input("Enter your guess: ")
        while len(user_word) != self.n_letters:
            print("The word must be 5 letters long.")
            user_word = input("Enter your guess: ")
        return user_word

    def display_match(self, user_word, match):
        for letter in match:
            print(self.symbols[letter], end="")
        print()

    def display_game_over(self, word_found, target_word):
        if word_found:
            print("Congratulations! You have found the word.")
        else:
            print("Game over. The correct word is:", target_word)