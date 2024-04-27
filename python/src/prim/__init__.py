from src.graph import Graph

class PrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = graph.vertices
        self.adjacency_list = graph.adjacency_list

    def find_mst(self):
        mst_edges = []
        mst_vertices = [self.vertices[0]]
        visited = {v: False for v in self.vertices}
        visited[self.vertices[0]] = True 

        while len(mst_vertices) < len(self.vertices):
            min_edge = None
            min_weight = float('inf')

            for v in mst_vertices: 
                for neighbor, weight in self.adjacency_list[v].items():
                    if not visited[neighbor] and weight < min_weight:
                        min_edge = (v, neighbor)
                        min_weight = weight

            mst_edges.append((min_edge[0], min_edge[1], min_weight))
            mst_vertices.append(min_edge[1])
            visited[min_edge[1]] = True

        mst_graph = Graph(self.vertices, mst_edges)
        return mst_graph
