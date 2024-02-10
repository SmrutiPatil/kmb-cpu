from src.graph import Graph
from src.kmb import KMB

# all vertices
vertices = [0, 1, 2, 3, 4, 5, 6, 7]

# (start_vertex, end_vertex, weight)
edges = [(0, 1, 3), (0, 2, 5), (0, 3, 7), (1, 4, 2), (1, 5, 4), (2, 6, 6), (2, 7, 8), (3, 4, 9), (4, 5, 11), (5, 6, 13), (6, 7, 15)]

# terminal vertices
terminal_vertices = [0,5,7]

graph = Graph(vertices, edges)

KMB(graph, terminal_vertices)





