# Implement Breadth-First Search in a graph
# Implement Depth-First Search in a graph

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add an edge to the graph (undirected by default)
    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    # Breadth-First Search
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        print("BFS Traversal:", end=" ")

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    # Depth-First Search (recursive)
    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self.dfs_util(start, visited)
        print()


# Example usage
g = Graph()
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6)]
for u, v in edges:
    g.add_edge(u, v)

# Perform BFS and DFS
g.bfs(0)
g.dfs(0)
