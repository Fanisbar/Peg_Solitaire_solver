# import matplotlib.pyplot as plt
# import numpy as np
from board import create_initial_board, apply_move
from problem import PegSolitaireProblem
from search import bfs, dfs

init_state = create_initial_board()
peg_solitaire = PegSolitaireProblem(init_state)
solution_moves = dfs(peg_solitaire)

solution_states = [init_state]
current = init_state
for move in solution_moves:
    current = apply_move(current, move)
    solution_states.append(current)

# def update(frame):
#     img.set_data(np.array(solution_states[frame]))
#     return img

# fig, ax = plt.subplots()
# img = ax.imshow(np.array(solution_states[0]))

for state in solution_states:
    for row in state:
        print(row)
    print("")
