import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        closed_list.add(current.name)

        for neighbour, cost in graph[current.name].items():
            if neighbour in closed_list:
                continue

            g = current.g + cost
            h = heuristics[neighbour]
            node = Node(neighbour, current, g, h)
            heapq.heappush(open_list, node)

    return None


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 4},
    'F': {'G': 1},
    'G': {}
}

heuristics = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 0
}

path = a_star(graph, heuristics, 'A', 'G')
print("Shortest path:", path)
