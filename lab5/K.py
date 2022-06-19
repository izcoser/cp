import sys

s = []
d = []

def f(t):
    ps = [s[i] * t + d[i] for i in range(len(s))]
    return max(ps) - min(ps)
    
def ternarySearch(l, r):
    for i in range(100):
        m1 = l + (r-l) / 3
        m2 = r - (r-l) / 3

        if f(m1) > f(m2):
            l = m1
        else:
            r = m2
    return f(l)

n, k = [int(i) for i in input().split()]
for i in range(n):
    ss, dd = [int(i) for i in input().split()]
    s.append(ss)
    d.append(dd)

print(f'{ternarySearch(0, k):.6f}')
