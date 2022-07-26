# Dijkstra shortest path implementation.

import heapq

def distance_u_v(graph, u, v):
    for (n, w) in graph[u]:
        if n == v:
            return w
    return float('INF')

graph = {
    # Node: [(Node, Weight), ...]
    0: [(1, 5), (7, 8), (4, 9)], 
    1: [(7, 4), (2, 12), (3, 15)],
    2: [(3, 3), (6, 11)],
    3: [(6, 9)],
    4: [(7, 5), (5, 4), (6, 20)],
    5: [(2, 1), (6, 13)],
    6: [],
    7: [(2, 7), (5, 6)],
}

def dijkstra(graph, s):
    distances = {i: float('INF') for i in graph}
    distances[s] = 0
    t = set()
    s = [(distances[i], i)  for i in graph]
    heapq.heapify(s)
    while len(s) > 0:
        v = heapq.heappop(s)[1]
        if v in t: # v is a duplicate.
            continue
        if t == len(graph): # already visited all nodes.
            break
        t.add(v)
        neighbors = [i[0] for i in graph[v]]
        for u in neighbors:
            d_vu = distance_u_v(graph, v, u)
            if u not in t and distances[u] > distances[v] + d_vu:
                distances[u] = distances[v] + d_vu
                heapq.heappush(s, (distances[u], u)) # add node u to heap again, the previous will be ignored.
    return distances

distances = dijkstra(graph, 0)
print(f'Distances from 0 to all other vertices: {distances}')
print('Uses a priority queue, log(V) for pop and E for iterating over neighbors.')
print('Time Complexity: E log(V).')