from src.graph import Graph
from src.dijkstra import Dijkstra
from src.prim import PrimMST

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

  # S3
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