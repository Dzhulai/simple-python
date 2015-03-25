"""
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))
for turn in range(4):
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break 
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"
    print "Turn", turn + 1     
    print_board(board)
    
"""

import random

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print "Turn: " + str(turn+1)
    guess_row = input("Guess Row: (0-4)")
    guess_col = input("Guess Col: (0-4)")

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship(S)!"
        board[ship_row][ship_col] = "S"
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."           
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == 3:
                print "Game Over (S = Battleship)"
                board[ship_row][ship_col] = "S"
                print_board(board)

