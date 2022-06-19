import sys

def score(i, ns):
    s = 1
    n = ns[i]
    prev = n
    for j in range(i + 1, len(ns)):
        if ns[j] <= prev:
            s += 1
            prev = ns[j]
        else:
            break

    prev = n
    for j in range(i - 1, -1, -1):
        if ns[j] <= prev:
            s += 1
            prev = ns[j]
        else:
            break

    return s
    
input()
ns = [int(i) for i in input().split()]

a = [score(i, ns) for i in range(len(ns))]
print(max(a))
