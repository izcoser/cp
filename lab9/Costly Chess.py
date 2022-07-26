import sys
import heapq

graph = {}

def distance_u_v(u, v):
    for (m, n, w) in graph[u]:
        if (m, n) == v:
            return w
    return float('INF')

def dijkstra(s, k):
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
        neighbors = [(i[0], i[1]) for i in graph[v]]
        for u in neighbors:
            d_vu = distance_u_v(v, u)
            if u not in t and distances[u] > distances[v] + d_vu:
                distances[u] = distances[v] + d_vu
                heapq.heappush(s, (distances[u], u)) # add node u to heap again, the previous will be ignored.

    if distances[k] < float('INF'):
        return distances[k]
    else:
        return -1

def knight_squares(i, j):
    return list(filter(lambda t: t[0] >= 0 and t[0] < 8 and t[1] >= 0 and t[1] < 8,
            [(i + 2, j + 1, i * (i + 2) + j * (j + 1)),
            (i + 1, j + 2, i * (i + 1) + j * (j + 2)),
            (i - 1, j + 2, i * (i - 1) + j * (j + 2)),
            (i - 2, j + 1, i * (i - 2) + j * (j + 1)),
            (i - 2, j - 1, i * (i - 2) + j * (j - 1)),
            (i - 1, j - 2, i * (i - 1) + j * (j - 2)),
            (i + 1, j - 2, i * (i + 1) + j * (j - 2)),
            (i + 2, j - 1, i * (i + 2) + j * (j - 1)),
            ]))

graph = {(i, j): knight_squares(i, j) for i in range(8) for j in range(8)}

for line in sys.stdin:
    a, b, c, d = [int(i) for i in line.split()]
    print(dijkstra((a, b), (c, d)))
