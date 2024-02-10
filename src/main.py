from graph import Graph
from dijkstra import Dijkstra
from prim import PrimMST

# Example usage:
vertices = [0, 1, 2, 3, 4, 5, 6, 7]
edges = [(0, 1, 3), (0, 2, 5), (0, 3, 7), (1, 4, 2), (1, 5, 4), (2, 6, 6), (2, 7, 8), (3, 4, 9), (4, 5, 11), (5, 6, 13), (6, 7, 15)]

terminal_vertices = [0,5,7]

def KMB(graph, terminal_vertices):

  graph.save_graph("graph.png")

  # S1
  graph1 = Graph(terminal_vertices, [])

  # S2
  added_edges = set()
  shortest_path_edges = {}
  for u in terminal_vertices:
      for v in terminal_vertices:
          if u != v:
              path, distance, edges = Dijkstra(graph).find_shortest_path(u, v)
              if (u,v) not in added_edges and (v,u) not in added_edges:
                shortest_path_edges[(u,v)] = edges
                graph1.add_edge(u,v,distance)
                added_edges.add((u,v))

  graph1.save_graph("graph1.png")

  # S2
  T1 = PrimMST(graph1).find_mst()

  T1.save_graph("t1.png")

  # S4
  vertices =  set() 
  for u,v in shortest_path_edges:
    for vertex in shortest_path_edges[(u,v)]:
      vertices.add(vertex[0])
      vertices.add(vertex[1])
  vertices = list(vertices)
  
  graph2 = Graph(vertices, [])

  for u,v in shortest_path_edges:
    for vertex in shortest_path_edges[(u,v)]:
      graph2.add_edge(vertex[0], vertex[1], vertex[2])
  graph2.save_graph("graph2.png")

  # S5

  steiner = PrimMST(graph2).find_mst()
  steiner.save_graph("steiner.png")

  # Visualize the graph

  graph.highlight_subgraph(steiner, terminal_vertices, filename = "kmb.png")

graph = Graph(vertices, edges)

KMB(graph, terminal_vertices)





