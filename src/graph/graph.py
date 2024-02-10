class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {v: {} for v in vertices}
        self.build_graph()

    def build_graph(self):
        for edge in self.edges:
            u, v, weight = edge
            # Add edge from u to v
            if v not in self.adjacency_list[u]:
                self.adjacency_list[u][v] = weight
            # Add edge from v to u
            if u not in self.adjacency_list[v]:
                self.adjacency_list[v][u] = weight

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list[v]:
            self.adjacency_list[u][v] = weight
        if v not in self.adjacency_list[u]:
            self.adjacency_list[v][u] = weight

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.adjacency_list[vertex] = {}
        
    def print_graph(self):
        print("Vertices:")
        for vertex in self.vertices:
            print(vertex)

        print("\nEdges:")
        printed_edges = set()
        for u, neighbors in self.adjacency_list.items():
            for v, weight in neighbors.items():
                if (u, v) not in printed_edges and (v, u) not in printed_edges:
                    print(f"{u} --({weight})-- {v}")
                    printed_edges.add((u, v))

        print("\nAdjacency List:")
        for vertex, neighbors in self.adjacency_list.items():
            temp = {x: neighbors[x] for x in neighbors}
            print(f"{vertex}: {temp}")
