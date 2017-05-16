import sys, tty, termios, os, csv

# ascII arts
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
E = '\033[33m'  # orange
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

sign_colours = {"X": G, "@": R}

def create_board():
    board = []
    with open('board_1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = list(row[0])
            board.append(row)

    return board

def get_coloured_sign(sign):
    if sign in sign_colours:
        return sign_colours[sign] + sign + R
    else:
        return sign

def print_board(board):
    """Prints board."""

    os. system("clear")
    for row in board:
        for sign in row:
            print(get_coloured_sign(sign), end="")
        print('')


def insert_player(board, y, x):
    """Inserts player in board in certain (x, y) position."""
    player = "@"
    board[y][x] = player

    return board
