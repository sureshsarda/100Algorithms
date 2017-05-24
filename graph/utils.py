"""
Load graph in memory as Adjacency Matrix
"""


def load(filename, directed=True):
    with open(filename, 'r') as f:
        vertices, edges = [int(i) for i in f.readline().split()]
        graph = [[0 for i in range(vertices)] for j in range(vertices)]
        for i in range(edges):
            record = [int(i) for i in f.readline().split()]
            s, t = record[0], record[1]  # Source, Target
            w = record[2] if len(record) > 2 else 1  # Weigth
            graph[s][t] = w
            if not directed:
                graph[t][s] = w
        return graph


def graph_print(graph):
    for i in graph:
        print(i, sep=' ')
