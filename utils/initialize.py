# This Function is responsible for Initializing the Board i.e 2D Array with all pieces in their original positions

def setup():
    board = []
    row1 = ['WR', 'WK', 'WB', 'WQ', 'WK', 'WB', 'WK', 'WR']
    row2 = ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp']
    # row6 = ['Wp']
    row7 = ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp']
    row8 = ['BR', 'BK', 'BB', 'BQ', 'BK', 'BB', 'BK', 'BR']
    board.append(row8)
    board.append(row7)
    for i in range(6):
        open_rows = []
        for j in range(8):
            open_rows.append('__')
        board.append(open_rows)
    board.append(row2)
    board.append(row1)
    return board
    print("Lets goo")

def print_board(board):
    for row in board:
        for column in row:
            print(column + ' ', end="")
        print()
