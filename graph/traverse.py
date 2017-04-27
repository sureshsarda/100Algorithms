import graph.utils as utils
from collections import deque


def traverse_bfs(graph):
    remaining = deque([0])  # Start
    sequence = []
    while remaining:
        current = remaining.popleft()
        sequence.append(current)
        for i, item in enumerate(graph[current]):  # Add not added, not visited entries
            if item and i not in sequence and i not in remaining:
                remaining.append(i)
    return sequence


def traverse_dfs(graph):
    remaining = deque([0])  # Start
    sequence = []
    while remaining:
        current = remaining.pop()
        sequence.append(current)
        for i, item in enumerate(graph[current]):  # Add not added, not visited entries
            if item and i not in sequence and i not in remaining:
                remaining.append(i)
    return sequence


for i in range(3):
    graph = utils.load('data/graph_0{0}.in'.format(i))

    print("Graph:")
    utils.graph_print(graph)
    print('BFS:')
    print(traverse_bfs(graph))
    print('DFS:')
    print(traverse_dfs(graph))
    print('*' * 80)
