# Implementation of Depth First Search and Breadth First Search.

graph = {'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'f', 'g'],
        'd': ['b'],
        'e': ['b'],
        'f': ['c', 'h'],
        'g': ['c'],
        'h': ['f'],
        }

visited = {i: False for i in 'abcdefgh'}

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for n in graph[v]:
        if not visited[n]:
            dfs(graph, n, visited)


def bfs(graph, v, visited):
    q = []
    q.append(v)
    while len(q) > 0:
        p = q.pop(0)
        visited[p] = True
        print(p, end=' ')
        for n in graph[p]:
            if not visited[n]:
                q.append(n)
    print()

print('Running DFS')
dfs(graph, 'a', visited)
print()

visited = {i: False for i in 'abcdefgh'}

print('Running BFS')
bfs(graph, 'a', visited)
