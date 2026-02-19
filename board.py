INVALID = -1
EMPTY = 0
PEG = 1

def create_initial_board():
    board = [
        [-1,-1, 1, 1, 1,-1,-1],
        [-1,-1, 1, 1, 1,-1,-1],
        [ 1, 1, 1, 1, 1, 1, 1],
        [ 1, 1, 1, 0, 1, 1, 1],
        [ 1, 1, 1, 1, 1, 1, 1],
        [-1,-1, 1, 1, 1,-1,-1],
        [-1,-1, 1, 1, 1,-1,-1],
    ]

    return tuple(tuple(row) for row in board)

# a move will be a tuple of 3 pairs of (x, y) coordinates on the board
def apply_move(state, move):
    (x1, y1), (x2, y2), (x3, y3) = move

    board = [list(row) for row in state]

    board[y1][x1] = EMPTY
    board[y2][x2] = EMPTY
    board[y3][x3] = PEG

    return tuple(tuple(row) for row in board)