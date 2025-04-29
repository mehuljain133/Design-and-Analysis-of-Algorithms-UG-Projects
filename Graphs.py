# Graphs: Graph Algorithms - Breadth First Search, Depth First Search and its Applications.

from collections import deque

# Graph traversal using BFS (Breadth-First Search)
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue for BFS
    
    visited.add(start)
    
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process current node
        
        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # For new line after BFS

# Graph traversal using DFS (Depth-First Search)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set
    
    visited.add(start)
    print(start, end=" ")  # Process current node
    
    # Explore neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
# Find all connected components in an undirected graph
def connected_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited=visited)
            components.append(list(visited))
    return components

# BFS for finding shortest path in an unweighted graph
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # Store path along with node
    
    visited.add(start)
    
    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            return path  # Return the shortest path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None  # Return None if no path exists

# Example Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# BFS Traversal
bfs(graph, 0)

# DFS Traversal
print("DFS Traversal:", end=" ")
dfs(graph, 0)
print()  # New line after DFS

# Connected Components (Using DFS)
components = connected_components(graph)
print("Connected Components:", components)

# Find Shortest Path using BFS
start_node = 0
goal_node = 3
shortest_path = bfs_shortest_path(graph, start_node, goal_node)
print(f"Shortest Path from {start_node} to {goal_node}:", shortest_path)
