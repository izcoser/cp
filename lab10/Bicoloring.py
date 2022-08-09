graph = {}
side = {}

while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    graph = {i: set() for i in range(n)}

    for i in range(m):
        a, b = [int(i) for i in input().split()]
        graph[a].add(b)
        graph[b].add(a)
        side[a] = -1
        side[b] = -1

    bipartido = True
    q = []
    for v in graph:
        if side[v] == -1:
            q.append(v)
            side[v] = 0
            while len(q) > 0:
                k = q.pop(0)
                for u in graph[k]:
                    if side[u] == -1:
                        side[u] = 0 if side[k] == 1 else 1
                        q.append(u)

                    else:
                        bipartido = (bipartido and (side[u] != side[k]))


    if bipartido:
        print('BICOLORABLE.')
    else:
        print('NOT BICOLORABLE.')