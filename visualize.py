import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.patches import Circle
import numpy as np

from board import create_initial_board, apply_move, INVALID, EMPTY, PEG
from problem import PegSolitaireProblem
from search import dfs

# solving the problem/game
init_state = create_initial_board()
peg_solitaire = PegSolitaireProblem(init_state)
solution_moves = dfs(peg_solitaire)

solution_states = [init_state]
current = init_state
for move in solution_moves:
    current = apply_move(current, move)
    solution_states.append(current)

# vizualisation

is_playing = False
current_index = 0
rows = len(solution_states[0])
cols = len(solution_states[0][0])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor("#8b5a2b")

ax.invert_yaxis()

patches = []

def draw_board(state):
    global patches
    
    for p in patches:
        p.remove()
    patches = []

    for r in range(rows):
        for c in range(cols):
            value = state[r][c]

            if value == INVALID:
                continue

            center = (c + 0.5, r + 0.5)

            hole = Circle(center, 0.4, color="#5c3a1e")
            ax.add_patch(hole)
            patches.append(hole)

            if value == PEG:
                peg = Circle(
                    center,
                    0.35,
                    facecolor="#004fa3",
                    edgecolor="#003b7a",
                    linewidth=2
                )
                ax.add_patch(peg)
                patches.append(peg)

    ax.set_title(f"Step {current_index}")
    fig.canvas.draw_idle()


draw_board(solution_states[current_index])


# Buttons

is_playing = False
timer = fig.canvas.new_timer(interval=1000)
timer.add_callback(lambda: play_loop())

def update_board():
    draw_board(solution_states[current_index])


def next_step(event=None):
    global current_index
    if current_index < len(solution_states) - 1:
        current_index += 1
        update_board()


def prev_step(event=None):
    global current_index
    if current_index > 0:
        current_index -= 1
        update_board()


def reset_board(event=None):
    timer.stop()
    global current_index, is_playing
    is_playing = False
    current_index = 0
    update_board()

def auto_play(event=None):
    global is_playing
    if not is_playing:
        is_playing = True
        timer.start()


def pause_play(event=None):
    global is_playing
    is_playing = False
    timer.stop()


def play_loop():
    global current_index, is_playing

    if not is_playing:
        return

    if current_index < len(solution_states) - 1:
        current_index += 1
        update_board()
    else:
        is_playing = False
        timer.stop()

ax_prev = plt.axes([0.05, 0.05, 0.12, 0.075])
ax_next = plt.axes([0.20, 0.05, 0.12, 0.075])
ax_auto = plt.axes([0.35, 0.05, 0.12, 0.075])
ax_pause = plt.axes([0.50, 0.05, 0.12, 0.075])
ax_reset = plt.axes([0.65, 0.05, 0.12, 0.075])

btn_prev = Button(ax_prev, 'Prev')
btn_next = Button(ax_next, 'Next')
btn_auto = Button(ax_auto, 'Auto')
btn_pause = Button(ax_pause, 'Pause')
btn_reset = Button(ax_reset, 'Reset')

btn_prev.on_clicked(prev_step)
btn_next.on_clicked(next_step)
btn_auto.on_clicked(auto_play)
btn_pause.on_clicked(pause_play)
btn_reset.on_clicked(reset_board)

plt.show()
