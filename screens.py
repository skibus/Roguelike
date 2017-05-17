#Level 1
def farm_1(board, y, x):
    board[6][4] = 'X'
    return board


def board_intro_csv(board):
   with open("board_1.csv", "w") as f:
       w = csv.writer(f, delimiter=' ')
       for item in board:
           w.writerow(item)


def csv_intro_board():
   board = []
   with open("board_1.csv", newline='') as f:
       r = csv.reader(f)
       for row in f:
           row = row.strip()
           row = list(row)
           board.append(row)
   return board