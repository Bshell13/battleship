"""
This script the game of battle ship.
Currently the game will only be one sided with the computer.
The plan is to play two sided with the computer.
Then to play two sided with someone on the same computer.
Finally, codding for an online version.

Creator: Brandon Shellenberger
Start Date: 2/24/2024
"""

from random import randint
import numpy as np

def create_board():
    """ Creates a board of 8X8 with @ and returns the np.array"""
    board = np.full((5, 6), '@')
    return board

def create_opp_board():
    """ Creates an opponent board with random ship placement"""
    opp_board = np.full((5, 6), 0)
    opp_col = randint(0, len(opp_board) - 1) #random int based on the baord length
    opp_row = randint(0, len(opp_board) - 1)
    opp_board[opp_row][opp_col] = 1
    return opp_board

def hit_make_mark(board, guess_row:int, guess_col:int):
    """ Makes hit marker at the guessed location
    param: board: numpy array
    param: guess_row: int from guess row
    param: guess_col: int from guess col"""
    board[guess_row - 1][guess_col - 1] = 'X'

def miss_make_mark(board, guess_row:int, guess_col:int):
    """ Makes miss marker at the guessed loaction
    param: board: numpy array
    param: guess_row: int from guess row
    param: guess_col: int from guess col"""
    board[guess_row - 1][guess_col - 1] = 'O'



def main():
    """ Main Function"""
    board = create_board()
    opp_board = create_opp_board()
    
    while True:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Column: "))
        
        
        if opp_board[guess_row - 1][guess_col - 1] == 1:
            hit_make_mark(board, guess_row, guess_col)
            print('Congratulations')
            return False
        else:
            miss_make_mark(board, guess_row, guess_col)
            print('Missed, try again!')
        
        print(board)


# Initializes the main function
if __name__ == "__main__":
    main()