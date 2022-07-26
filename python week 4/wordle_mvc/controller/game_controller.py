from view.game_view import GameView
from model.wordle_game import WordleGame

class GameController:
    def __init__(self, model: WordleGame, view: GameView):
        self.model = model
        self.view = view

    def run_game(self):
        self.view.display_welcome_message()
        self.model.select_target_word()

        curr_guess = 1
        user_word = self.view.get_user_word()
        while not self.model.is_terminated(user_word, curr_guess):
            match = self.model.check_guess(user_word)
            self.view.display_match(user_word, match)
            user_word = self.view.get_user_word()
            curr_guess += 1

        if curr_guess == self.model.n_guesses:
            self.view.display_game_over(False, self.model.target_word)
        else:
            self.view.display_game_over(True, self.model.target_word)

