import sys, tty, termios, os


width = int(input('Write the width: '))
height = int(input('Write the height: '))

def create_board(width, height):
    h = []
    w = []
    w2 = []
    for el in range(width):
        w.append('X')
    for el in range(height - 2):
        h1 = []
        h.append(h1)
        for el in range(width):
            if el == 0 or el == width - 1 :
                h1.append('X')
            else:
                h1.append(' ')

    for el in range(width):
        w2.append('X')

    board = [w, *h, w2]
    return board

def print_board(board):
    os.system('clear')
    for el in board:
        print (*el)

def insert_char(board,y,x):
    board[y][x] = '@'
    return board


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    char_y = 1
    char_x = 1
    board = create_board(width, height)
    print (board)
    insert_char(board, char_y, char_x)
    print_board(board)
    x = getch()

    while x != 'q':
        x = getch()
        if x == 's':
            if board[char_y + 1][char_x] != 'X':
                char_y += 1
        elif x == 'w':
            if board[char_y -1][char_x] != 'X':
                char_y -= 1
        elif x == 'a':
            if board[char_y][char_x - 1] != 'X':
                char_x -= 1
        elif x == 'd':
            if board[char_y][char_x + 1] != 'X':
                char_x += 1
        elif x == 'q':
            sys.exit()

        board = create_board(width, height)
        insert_char(board, char_y, char_x)
        print_board(board)

if __name__ == '__main__':
    main()

a

#def print_board(board):
