graph = {}
weight = {}

def duv(u, v):
    if (u, v) in weights:
        return weight[(u, v)]
    return float('INF')

def bellman_ford(s):
    d = {v: float('INF') for v in graph} # distance from s to all other nodes
    d[s] = 0
    for _ in range(len(graph) -1):
        for (u, v) in weight:
            w = weight[(u, v)]
            if d[u] + w < d[v]:
                d[v] = d[u] + w

    for(u, v) in weight:
        w = weight[(u, v)]
        if d[u] + w < d[v]:
            return 'possible'
    return 'not possible'

for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    graph = {}
    weight = {}
    for i in range(m):
        a, b, c = [int(i) for i in input().split()]
        graph[a] = b
        weight[(a, b)] = c

    print(bellman_ford(0))
