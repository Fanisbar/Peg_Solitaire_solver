from problem import PegSolitaireProblem
from board import create_initial_board

# testing

problem = PegSolitaireProblem(create_initial_board())
succ = problem.get_successors(problem.get_start_state())
print(len(succ))
