class graph:
    def __init__(self):
        self.adj_list = {}
        self.visited = set()

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs_recursive(self, current):
        print(current, end=" ")
        self.visited.add(current)
        for neighbour in self.adj_list[current]:
            if neighbour not in self.visited:
                self.dfs_recursive(neighbour)

    def dfs(self, start):
        self.visited = set()
        print("dfs traversal")
        self.dfs_recursive(start)

g = graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('C','E')
g.dfs('A')
print("\nVTU29648")
