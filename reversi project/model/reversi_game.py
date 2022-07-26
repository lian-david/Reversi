from model.board import Board
from model.players import Players

class ReversiGame:
    """Represents game. Including board, players, 
        classical rules, alternative rules.
    """
    def __init__(self, board_size):
        #board_size = ReversiUser.get_board_size()
        # rules = ReversiUser.get_rules()
        # self.rules = rules

        self.board = Board(board_size)
        self.curr_player = None
        self.black_disk = Players.BLACK_DISK
        self.white_disk = Players.WHITE_DISK
        self.score_book = {}

    def change_player(self):
        """Changes player, used for each turn of the game.
        """
        if self.curr_player is None:
            self.curr_player = self.black_disk
        else:
            if self.curr_player == self.black_disk:
                self.curr_player = self.white_disk
            else:
                self.curr_player = self.black_disk

    def is_valid_move(self, row, col):
        """Determines if move is valid.
        
        Returns:
                T/F if player's move is valid according to classical rules.
                spaces_flip(list): list of locations if the move is valid.
        """
        if self.board._board[row][col] != self.board.EMPTY_CELL or not self.board.valid_location(row, col):
            return False
        self.board._board[row][col] = self.curr_player     #set player in location for checking
        if self.curr_player == Players.BLACK_DISK:
            other_play = Players.WHITE_DISK
        else:
            other_play = Players.BLACK_DISK

        spaces_flip = []
        #all possible directions to move row, col
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for row_direct, col_direct in directions:
            r, c = row, col
            r += row_direct
            c += col_direct
            #determines if there is other player's disk next to our disk
            if self.board.valid_location(r, c) and self.board._board[r][c] == other_play:
                r += row_direct
                c += col_direct
                if not self.board.valid_location(r, c):
                    continue
                while self.board._board[r][c] == other_play:
                    r += row_direct
                    c += col_direct
                    if not self.board.valid_location(r, c):
                        break
                if not self.board.valid_location(r, c):
                    continue
                #locate pieces to flip and add locations to list 
                if self.board._board[r][c] == self.curr_player:
                    while True:
                        r -= row_direct
                        c -= col_direct
                        if r == row and c == col:
                            break
                        spaces_flip.append([r, c])

        #return empty location after performing possible move
        self.board._board[row][col] = self.board.EMPTY_CELL
        #return F for no spaces to flip
        if len(spaces_flip) == 0:
            return False
        
        return spaces_flip

        #for alt rules just return spaces flip without checking len?

    def make_move(self, row, col):
        """Makes move if it is valid.
        """
        spaces_flip = self.is_valid_move(row, col)
        if spaces_flip == False:
            return False
        
        self.board.update_location(row, col, self.curr_player)
        for r, c in spaces_flip:
            self.board.update_location(r, c, self.curr_player)
        return True
        #spaces_flip = self.is_valid_move(row, col)
        # if spaces_flip:
        #     self.board.update_location(row, col, self.curr_player)
        #     for r, c in spaces_flip:
        #         self.board.update_location(r, c, self.curr_player)
        # else:
        #     return False


    def get_scores(self):
        """Calculates scores for each user

        Returns:
            score_book(dict): dictionary of player scores
        """
        black_score = 0
        white_score = 0
        for r in range(self.board.size):
            for c in range(self.board.size):
                if self.board.get_location(r, c) == Players.BLACK_DISK:
                    black_score += 1
                if self.board.get_location(r, c) == Players.WHITE_DISK:
                    white_score += 1

        self.score_book = {"X":black_score, "O":white_score}
        return self.score_book

    def get_winner(self):
        """Calculates winning score from score book

        Returns:
            winner(player): player with the winning score / tie
        """
        scores = self.score_book
        black_score = scores["X"]
        white_score = scores["O"]

        if black_score > white_score:
            self.winner = Players.BLACK_DISK
        elif white_score > black_score:
            self.winner = Players.WHITE_DISK
        elif black_score == white_score:
            self.winner = 3

        return self.winner

    def is_terminated(self, row, col):
        if self.make_move(row, col) == False:
            return True

        
