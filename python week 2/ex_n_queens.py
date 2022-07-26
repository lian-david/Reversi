#problem of placing N chess queens on an N × N chessboard so that no two queens attack each other

N = int(input("Enter the number of queens: "))
board = [[0]* N for i in range (N)]
all_placements = []

def is_attack(row, col):
    #check if queen is in row or col
    for q in range(0, N):
        if board[row][q] == 1 or board[q][col] == 1:
            return True
    #check if queen is in diagonals
    for q in range(0, N):
        for i in range(0, N):
            if(q + i == row + col) or (q - i == row-col):
                if board[q][i] == 1:
                    return True

    return False

def place_queens(n):
    #base case: solution found
    if n == 0:
        return True
    for row in range(0, N):
        for col in range(0, N):
            #placing queen if space is unoccupied/not under attack
            if (not (is_attack(row, col))) and (board[row][col] != 1):
                board[row][col] = 1
                if place_queens(n - 1) == True:
                    return True
                board[row][col] = 0

    return False

def q_board():
    place_queens(N)
    for q in board:
        print(q)

q_board()





# def is_safe(row, col):
#     for i in range(n):
#         if board[row][i] == 1:
#             return False
#     for j in range(n):
#         if board[j][col] == 1:
#             return False 

#     #check if Q is placed in any directions
#     i = row - 1
#     j = col - 1
#     while(i >= 0 and j>=0):
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j -= 1

#     i = row - 1
#     j = col + 1
#     while(i >= 0 and j < n):
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j += 1

#     i = row + 1
#     j = col - 1
#     while(i < n and j >= 0):
#         if board[i][j] == 1:
#             return False
#         i += 1
#         j -= 1

#     i = row + 1
#     j = col + 1
#     while(i < n and j < n):
#         if board[i][j] == 1:
#             return False 
#         i += 1
#         j += 1

#     return True     #if queen passes all checks 