
import numpy as np
import pandas as pd

def my_board_ships():
    '''
    User places their ships in locations
    Things to do:
    - Check for spelling (ship_choice and direction)
    - Check if space is on board
    - Check for fitting (does the ship fit on the board)
    - Loop all 5 tiems
    '''
    # Ship names with number of spaces
    ship_data = {'name': ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer'],
                 'spaces': [5, 4, 3, 3, 2]}
    ships_df = pd.DataFrame(ship_data)
    letter_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    while True:
        ship_choice = input('Pick a ship (Carrier, Battleship, Cruiser, Submarine, Destroyer): ')
        if ship_choice not in ship_data['name']:
            print('Please type one of the ship named above: ')
        else:
            False
    starting_place = input('Name a coordinate on where you want your ship to start: ')
    # Slices letter and number
    placement_letter = starting_place[0]
    placement_num = int(starting_place[1])
    direction = input('Which direction would you like your ship to face (Left, Right, Up, Down): ')
    
    placement_data = [ship_choice, placement_letter, placement_num, direction]
    
    my_board[letter_index[placement_data[1]]][placement_data[2] - 1] = 1
    

def board(dimensions: int):
    '''
    Returns an array of zeros
    Needing to add:
    1. variability of board size
    2. eliminate brackets
    '''
    return np.zeros(dimensions, dtype=int)

def main():
    global my_board, opp_board
    my_board = (board(dimensions = (10,10)))
    opp_board = (board(dimensions = (10,10)))
    
    my_board_ships()
    
    print(my_board)


# entry into the main block of code
if __name__ == '__main__':
    main()