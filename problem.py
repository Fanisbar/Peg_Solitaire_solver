from board import INVALID, EMPTY, PEG, apply_move

class SearchProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_start_state(self):
        return self.initial_state

    def is_goal_state(self, state):
        count = sum(cell == PEG for row in state for cell in row)
        return count == 1

    def get_successors(self, state):
        successors = []

        directions = [(0,1),   # up
                    (0,-1),    # down
                    (-1,0),    # left
                    (1,0)]     # right
        
        # for every peg
        for y1 in range(len(state)):
            for x1 in range(len(state[0])):

                if state[y1][x1] != PEG:
                    continue
                # for every direction
                for (dx, dy) in directions:
                    x2 = x1+dx
                    y2 = y1+dy
                    x3 = x1+dx+dx
                    y3 = y1+dy+dy
                    if self.is_valid_move(state, x1, y1, x2, y2, x3, y3):
                        move = ((x1, y1), (x2, y2), (x3, y3))
                        succ = apply_move(state, move)
                        successors.append((succ, move, 1))
        return successors

    def is_valid_move(self, state, x1, y1, x2, y2, x3, y3):
        if x3<0 or y3<0 or x3>=len(state[0]) or y3>=len(state) or x2<0 or y2<0 or x2>=len(state[0]) or y2>=len(state):
            return False
        
        return state[y1][x1] == PEG and state[y2][x2] == PEG and state[y3][x3] == EMPTY

class PegSolitaireProblem(SearchProblem):
    pass
