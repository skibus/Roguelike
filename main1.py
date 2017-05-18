import sys, tty, termios, os, time
from random import randint
from create_board import create_board, print_board
from update_inventory import print_table, add_item_to_inventory, inventory, added_items #add_to_inventory
# from screens import        
from characters import insert_player, insert_dog, insert_farmer



def getch():
    '''Launches the keys'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch



def makes_good_step(y, x, y_next_step, x_next_step):
    '''Moves main character''' 

    y += y_next_step
    x += x_next_step
    
    return y, x



def check_next_step(y, x, barriers, board):
    '''Check the correctness of the next step'''

    return board[y][x] not in barriers



def set_direction(key_direction):
    '''Determines the value and direction of the hero's movement'''

    if key_direction == "w":
        x_direction = 0
        y_direction = -1
        inventory['stamina'] -= 1

    elif key_direction == "s":
        x_direction = 0
        y_direction = 1
        inventory['stamina'] -= 1

    elif key_direction == "a":
        x_direction = -1
        y_direction = 0
        inventory['stamina'] -= 1

    elif key_direction == "d":
        x_direction = 1
        y_direction = 0
        inventory['stamina'] -= 1

    else:
        x_direction = 0
        y_direction = 0


    return x_direction, y_direction



def handles_first_level():
    
    os.system("clear")
    x_current_position = 1  
    y_current_position = 1
    board = create_board('level_1.csv')
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position
        print (y_current_position, x_current_position)

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = makes_good_step(y_current_position, x_current_position, y_direction, x_direction)
        
        if inventory['dollars'] == 40:
            board[8][60] = "∃"            
        
        if board[y_current_position][x_current_position] == '∃':
            handles_second_level()    

        elif key_direction == "q":
            sys.exit()

        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)
        print_board(board)
        print_table(inventory)
        



def handles_second_level():
    """Handle game's second level game."""

    os.system("clear")
    x_current_position = 1  #starting position of player
    y_current_position = 1
    board = create_board("level_1.csv")
    last_hero_position = board[y_current_position][x_current_position]

    barriers = ['X','⌂','🚪']
    added_items = []

    key_direction = getch()  #control

    while key_direction != "q":
        x_direction = 0
        y_direction = 0

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = makes_good_step(y_current_position, x_current_position, y_direction, x_direction)

        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)
        print_board(board)


      

if __name__ == '__main__':
    handles_first_level()
