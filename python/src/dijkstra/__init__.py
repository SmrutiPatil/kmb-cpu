import heapq

class Dijkstra:
    def __init__(self, graph):
        self.vertices = graph.vertices
        self.adjacency_list = graph.adjacency_list

    def find_shortest_path(self, start, end):
        pq = [(0, start)]
        dist = {vertex: float('inf') for vertex in self.vertices} 
        dist[start] = 0
        prev = {vertex: None for vertex in self.vertices} 

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_dist > dist[current_vertex]: 
                continue

            if current_vertex == end:
                path = []
                edges = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    if prev[current_vertex] is not None:
                        edges.append((prev[current_vertex], current_vertex, self.adjacency_list[prev[current_vertex]][current_vertex]))
                    current_vertex = prev[current_vertex]
                path.reverse()
                edges.reverse()
                return path, dist[end], edges

            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return None, float('inf'), None
