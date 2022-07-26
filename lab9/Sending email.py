import heapq

graph = {}

def distance_u_v(u, v):
    for (n, w) in graph[u]:
        if n == v:
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
        neighbors = [i[0] for i in graph[v]]
        for u in neighbors:
            d_vu = distance_u_v(v, u)
            if u not in t and distances[u] > distances[v] + d_vu:
                distances[u] = distances[v] + d_vu
                heapq.heappush(s, (distances[u], u)) # add node u to heap again, the previous will be ignored.

    if distances[k] < float('INF'):
        return str(distances[k])
    else:
        return 'unreachable'

for case in range(int(input())):
    n, m, s, t = [int(i) for i in input().split()]
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        a, b, c = [int(i) for i in input().split()]
        graph[a].append((b, c))
        graph[b].append((a, c))

    print('Case #' + str(case+ 1) + ': ' + dijkstra(s, t))
