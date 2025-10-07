import heapq


graph = {
    'S': {'A': 2, 'B': 3},
    'A': {'G': 3},
    'B': {'G': 2},
    'G': {}
}


heuristic = {
    'S': 5,
    'A': 2,
    'B': 3,
    'G': 0
}

def a_star(start, goal):
    
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        
        if node == goal:
            return path, g

    
        for neighbor, cost in graph[node].items():
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")


path, cost = a_star('S', 'G')
print("Shortest path:", path)
print("Total cost:", cost)
