from model.reversi_game import ReversiGame
import copy

class AI:
    def __init__(self, game: ReversiGame):
        """Initializes AI Player attributes"""
        self.game = game
        self.board = self.game.board

    def computer_move(self):
        """Returns best move for computer to make based on one step lookahead

        Returns:
            best_move(tuple): row and column indices for computer play 
        """
        valid_moves = self.game.get_moves()
        best_score = -1
        for r,c in valid_moves:
            board_copy = copy.deepcopy(self.board)
            board_copy.update_location(r, c, self.game.curr_player)
            
            black_score = board_copy.score_book["X"]
            white_score = board_copy.score_book["O"]
            score = white_score - black_score
            if score > best_score:
                best_move = r, c
                best_score = score
        
        if best_move:
            return best_move
