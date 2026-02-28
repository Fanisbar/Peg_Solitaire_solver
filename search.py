from utils import Queue, Stack
from problem import SearchProblem

def bfs(problem=SearchProblem):
    if problem.is_goal_state(problem.get_start_state()):
        return []
    queue_f = Queue()
    # every tuple in the queue has a state and a path to that item
    queue_f.push((problem.get_start_state(), []))
    # set of expanded nodes (not to be visited twice)
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

def dfs(problem=SearchProblem):
    if problem.is_goal_state(problem.get_start_state()):
        return []
    queue_f = Stack()
    # every tuple in the queue has a state and a path to that item
    queue_f.push((problem.get_start_state(), []))
    # set of expanded nodes (not to be visited twice)
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

def a_star(problem):
    pass

def uniform_cost(problem):
    pass

