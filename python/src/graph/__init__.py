import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {v: {} for v in vertices}
        self.build_graph()

    def build_graph(self):
        for edge in self.edges:
            u, v, weight = edge
            if v not in self.adjacency_list[u]:
                self.adjacency_list[u][v] = weight
            if u not in self.adjacency_list[v]:
                self.adjacency_list[v][u] = weight

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list[v]:
            self.adjacency_list[u][v] = weight
        if v not in self.adjacency_list[u]:
            self.adjacency_list[v][u] = weight
        self.edges.append((u, v, weight))

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
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

    def save_graph(self, filename="graph.png"):
        G = nx.Graph()
        G.add_nodes_from(self.vertices)
        G.add_weighted_edges_from(self.edges)
        
        pos = nx.spring_layout(G)  
        labels = {edge[:2]: edge[2] for edge in self.edges}
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='black', linewidths=1, font_size=12)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
        plt.title("Graph Visualization")
        plt.savefig(filename)

    def highlight_subgraph(self, subgraph, terminal_vertices, filename="highlighted_graph.png"):
        G = nx.Graph()
        G.add_nodes_from(self.vertices)
        G.add_weighted_edges_from(self.edges)

        subgraph_nodes = set(subgraph.vertices)
        subgraph_edges = set(subgraph.edges)
        subgraph_terminal_vertices = set(terminal_vertices)

        pos = nx.spring_layout(G)

        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='black', linewidths=1, font_size=12)

        nx.draw_networkx_nodes(G, pos, nodelist=subgraph_nodes, node_color='red', node_size=700)
        nx.draw_networkx_nodes(G, pos, nodelist=subgraph_terminal_vertices, node_color='green', node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=subgraph_edges, edge_color='red', width=2)

        plt.text(0.05, 0.95, 'Blue: Original Graph', color='blue', transform=plt.gca().transAxes)
        plt.text(0.05, 0.90, 'Green: Terminals', color='green', transform=plt.gca().transAxes)
        plt.text(0.05, 0.85, 'Red: Non Terminals & steiner tree path', color='red', transform=plt.gca().transAxes)
        plt.title("Graph with Highlighted Subgraph")
        plt.savefig(filename)


