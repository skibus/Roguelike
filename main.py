import sys, tty, termios, os, time
from create_board import create_board, print_board, insert_player

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("dfdfefffff")



def main():
    # os.system("clear")
    y = 1 #starting position of player
    x = 1
    board = create_board()
    direct = getch()

    while direct != 'q':
        direct = getch()
        if direct == 'w':
            if board[y-1][x] != "X":
                y -= 1
        if direct == 's':
            if board[y+1][x] != "X":
                y += 1
        if direct == 'd':
            if board[y][x+1] != "X":
                x += 1
        if direct == "a":
            if board[y][x-1] != "X":
                x -= 1
        if direct == 'q':
            sys.exit()

        board = create_board()
        insert_player(board, y, x)
        print_board(board)


if __name__ == '__main__':
    main()
