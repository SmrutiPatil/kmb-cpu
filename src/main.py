from graph.graph import Graph
from dijkstra.dijkstra import Dijkstra

# Example usage:
vertices = [0,1,2,3]
edges = [(0,1, 5), (0,2, 2), (2,3, 10), (1,3, 20)]

terminal_vertices = [0,3]

def KMB(graph, terminal_vertices):
  # S1
  graph1 = Graph(terminal_vertices, [])

  # S2
  graph2 = Graph([], [])

  # S3
  added_edges = set()
  for u in terminal_vertices:
      for v in terminal_vertices:
          if u != v:
              path, distance = Dijkstra(graph.vertices, graph.adjacency_list).find_shortest_path(u, v)
              if (u,v) not in added_edges and (v,u) not in added_edges:
                graph1.add_edge(u,v,distance)
                added_edges.add((u,v))

graph = Graph(vertices, edges)

KMB(graph, terminal_vertices)





