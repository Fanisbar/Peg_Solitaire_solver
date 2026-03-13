from utils import Queue, Stack
from problem import SearchProblem

def _graph_search(problem: SearchProblem, frontier):
    start_state = problem.get_start_state()
    if problem.is_goal_state(start_state):
        return []

    frontier.push((start_state, []))
    visited = {start_state}

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if problem.is_goal_state(state):
            return path

        for next_state, move, _ in problem.get_successors(state):
            if next_state in visited:
                continue
            visited.add(next_state)
            frontier.push((next_state, path + [move]))

    return []


def bfs(problem: SearchProblem):
    return _graph_search(problem, Queue())

def dfs(problem: SearchProblem):
    return _graph_search(problem, Stack())

def a_star(problem):
    pass

def uniform_cost(problem):
    pass
