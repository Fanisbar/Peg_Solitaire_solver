INVALID = -1
EMPTY = 0
PEG = 1

def create_board(size=7):
    if size not in (5, 7, 9):
        raise ValueError("Board size must be one of: 5, 7, 9")

    corner = (size - 3) // 2
    board = [[PEG for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            in_top_or_bottom = y < corner or y >= size - corner
            in_left_or_right = x < corner or x >= size - corner
            if in_top_or_bottom and in_left_or_right:
                board[y][x] = INVALID

    center = size // 2
    board[center][center] = EMPTY

    return tuple(tuple(row) for row in board)


def create_initial_board(size=7):
    return create_board(size)

# a move will be a tuple of 3 pairs of (x, y) coordinates on the board
def apply_move(state, move):
    (x1, y1), (x2, y2), (x3, y3) = move

    board = [list(row) for row in state]

    board[y1][x1] = EMPTY
    board[y2][x2] = EMPTY
    board[y3][x3] = PEG

    return tuple(tuple(row) for row in board)