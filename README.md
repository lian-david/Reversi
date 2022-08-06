Reversi Game (also known as Othello)

This game supports varying players and game logic across board size of choice. 
AI player implemented with simple algorithm (one step lookahead) and advanced algorithm (MiniMax).

The game logic is as follows:
    A player's move is valid if it causes flips of the opponent's disks.
    If one player cannot make a valid move, the play is passed to the other player. 
    When neither player can make a move, the game ends. 
This logic is applied in the alternative setting of the game, although the validity 
    of the moves is catered to allow players to place disks in empty squares that
    do not cause flips of the opponent's disks.  