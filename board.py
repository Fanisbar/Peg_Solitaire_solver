INVALID = -1
EMPTY = 0
PEG = 1

def create_english_board():
    board = [[PEG for _ in range(7)] for _ in range(7)]
    for y in range(7):
        for x in range(7):
            if (y < 2 or y > 4) and (x < 2 or x > 4):
                board[y][x] = INVALID
    board[3][3] = EMPTY
    return tuple(tuple(row) for row in board)

def create_fireplace_board():
    board = [[INVALID for _ in range(7)] for _ in range(7)]
    valid_cells = [
               (1,2), (1,3), (1,4),
               (2,2), (2,3), (2,4),
        (3,1), (3,2), (3,3), (3,4), (3,5),
        (4,1), (4,2), (4,3), (4,4), (4,5)
    ]
    for y, x in valid_cells:
        board[y][x] = PEG

    board[4][3] = EMPTY
    return tuple(tuple(row) for row in board)

def create_pyramid_board():
    board = [[EMPTY for _ in range(7)] for _ in range(7)]
    
    for y in range(7):
        for x in range(7):
            if (y < 2 or y > 4) and (x < 2 or x > 4):
                board[y][x] = INVALID
                
    pegs = [
        (0, 4), (1, 4),
        (2, 5),
        (3, 1), (3, 2),
        (3, 4), (3, 5),
        (4, 1), (4, 2)
    ]
    
    for (y, x) in pegs:
        board[y][x] = PEG
        
    return tuple(tuple(row) for row in board)

def create_diamond_board():
    board = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,0,1,1,1],
        [0,1,1,1,1,1,0],
        [0,0,1,1,1,0,0],
        [0,0,0,1,0,0,0]
    ]
    return tuple(tuple(row) for row in board)

def apply_move(state, move):
    (x1, y1), (x2, y2), (x3, y3) = move

    board = [list(row) for row in state]

    board[y1][x1] = EMPTY
    board[y2][x2] = EMPTY
    board[y3][x3] = PEG

    return tuple(tuple(row) for row in board)