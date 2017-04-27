"""
Load graph in memory as Adjacency Matrix
"""


def load(filename, directed=True):
    with open(filename, 'r') as f:
        vertices, edges = [int(i) for i in f.readline().split()]
        graph = [[0 for i in range(vertices)] for j in range(vertices)]
        for i in range(edges):
            s, t = [int(i) for i in f.readline().split()]  # Source, Target
            graph[s][t] = 1
            if not directed:
                graph[t][s] = 1
        return graph


def graph_print(graph):
    for i in graph:
        print(i, sep=' ')