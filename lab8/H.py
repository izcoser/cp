# Runtime error on Vjudge, but passes all times.

forbidden = set()

def neighbors(v):
    n = []
    digits = [i for i in v]
    for i in range(4):
        n1 = digits.copy()
        n2 = digits.copy()

        a = int(n1[i]) + 1
        n1[i] = str(a) if a <= 9 else '0'

        b = int(n2[i]) - 1
        n2[i] = str(b) if b >= 0 else '9'
        
        n.append(''.join(n1))
        n.append(''.join(n2))
    return n

def bfs_with_depth(v, goal):
    if v == goal:
        print(0)
        return
        
    visited = set(forbidden)
    depth = 0
    q = []
    q.append(v)
    visited.add(v)
    while len(q) > 0:
        depth_size = len(q)
        while depth_size > 0:
            p = q.pop(0)

            for n in [i for i in neighbors(p) if i not in forbidden and i not in visited]:
                if n == goal:
                    print(depth + 1)
                    return
                q.append(n)
                visited.add(n)
            depth_size -= 1
        depth += 1
    print(-1)

cases = int(input())
for c in range(cases):
    initial = input().strip().replace(' ', '')
    goal = input().strip().replace(' ', '')
    
    for i in range(int(input())):
        n = input().strip().replace(' ', '')
        forbidden.add(n)

    bfs_with_depth(initial, goal)

    if c != cases -1:
        input()
    forbidden = set()
