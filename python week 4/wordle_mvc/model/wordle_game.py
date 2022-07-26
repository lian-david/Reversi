from model.word_bank import WordBank
from model.letter_type import LetterType

class WordleGame:
    """This class implements the wordle game model 
    """
    def __init__(self, wordle_file="sgb-words.txt", n_letters=5, n_guesses=6):
        self.wordle_list = WordBank(wordle_file)
        self.n_letters = n_letters
        self.n_guesses = n_guesses

    def select_target_word(self):
        self.target_word = self.wordle_list.select_random_word()
        return self.target_word

    def check_guess(self, user_word):
        letters_left = list(self.target_word)   #list of letters that need to be found
        #mark incorrect letters to start, gray letters
        match = [LetterType.INCORRECT_LETTER] * self.n_letters

        #mark correct letters, green letters
        for i in range(len(user_word)):
            if user_word[i] == self.target_word[i]:
                match[i] = LetterType.CORRECT_PLACE
                letters_left.remove(user_word[i])

        #mark correct letters wrong place, yellow letters
        for i in range(len(user_word)):
            if user_word[i] in letters_left and match[i] != LetterType.CORRECT_PLACE:
                match[i] = LetterType.CORRECT_LETTER
                letters_left.remove(user_word[i])

        return match

    def is_terminated(self, user_word, curr_guess):
        return self.target_word == user_word or curr_guess > self.n_guesses
    