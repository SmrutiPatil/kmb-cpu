from graph import Graph

class PrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = graph.vertices
        self.adjacency_list = graph.adjacency_list

    def find_mst(self):
        mst_edges = []  # Store the edges of the MST
        mst_vertices = [self.vertices[0]]  # Start with the first vertex
        visited = {v: False for v in self.vertices}  # Mark all vertices as not visited
        visited[self.vertices[0]] = True  # Mark the first vertex as visited

        while len(mst_vertices) < len(self.vertices):
            min_edge = None
            min_weight = float('inf')

            # Iterate through all vertices in the MST
            for v in mst_vertices:
                # Iterate through adjacent vertices of v
                for neighbor, weight in self.adjacency_list[v].items():
                    if not visited[neighbor] and weight < min_weight:
                        min_edge = (v, neighbor)
                        min_weight = weight

            # Add the min weight edge to the MST
            mst_edges.append((min_edge[0], min_edge[1], min_weight))
            mst_vertices.append(min_edge[1])
            visited[min_edge[1]] = True

        # Create a new graph object for MST
        mst_graph = Graph(self.vertices, mst_edges)
        return mst_graph
