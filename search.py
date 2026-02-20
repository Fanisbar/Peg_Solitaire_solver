from utils import Queue
from problem import SearchProblem

def bfs(problem=SearchProblem):
    if problem.is_goal_state(problem.get_start_state()):
        return []
    queue_f = Queue()
    queue_f.push((problem.getStartState(), []))
    expanded = set()

    while not queue_f.isEmpty():
        graph_node = queue_f.pop()
        if problem.is_goal_state(graph_node[0]):
            return graph_node[1]
        if graph_node[0] not in expanded:
            expanded.add(graph_node[0])
            for child in problem.get_successors(graph_node[0]):
                new_path = graph_node[1] + [child[1]]
                queue_f.push((child[0], new_path))

    return []

def dfs(problem):
    pass

def a_star(problem):
    pass

def uniform_cost(problem):
    pass
