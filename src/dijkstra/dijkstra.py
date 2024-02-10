import heapq

class Dijkstra:
    def __init__(self, vertices, adjacency_list):
        self.vertices = vertices
        self.adjacency_list = adjacency_list

    def find_shortest_path(self, start, end):
        pq = [(0, start)]  # Priority queue to store vertices with their distances from start
        dist = {vertex: float('inf') for vertex in self.vertices}  # Initialize distances
        dist[start] = 0

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_dist > dist[current_vertex]:  # If outdated vertex is encountered, ignore
                continue

            if current_vertex == end:
                path = [end]
                while end != start:
                    for neighbor, weight in self.adjacency_list[end].items():
                        if dist[end] == dist[neighbor] + weight:
                            path.append(neighbor)
                            end = neighbor
                            break
                return list(reversed(path)), dist[current_vertex]

            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return None, float('inf')
