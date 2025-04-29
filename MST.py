# Write a program to determine the minimum spanning tree of a graph

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Graph:
    def __init__(self):
        self.edges = []  # (weight, u, v)
        self.vertices = set()

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
        self.vertices.add(u)
        self.vertices.add(v)

    def kruskal_mst(self):
        mst = []
        total_weight = 0
        ds = DisjointSet(self.vertices)

        # Sort edges by weight
        self.edges.sort()

        for weight, u, v in self.edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, weight))
                total_weight += weight

        return mst, total_weight

# Example usage
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

mst_edges, mst_weight = g.kruskal_mst()

print("Minimum Spanning Tree edges:")
for u, v, weight in mst_edges:
    print(f"{u} - {v}: {weight}")
print("Total weight of MST:", mst_weight)
