n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
ms = []
for i in range(m):
    ms.append(int(input()))
s = set()
distinct = {}
for i in reversed(a):
    s.add(i)
    distinct[n] = len(s)
    n -= 1
for i in ms:
    print(distinct[i])