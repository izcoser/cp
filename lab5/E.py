import sys

r1, r2 = [int(i) for i in input().split()]
c1, c2 = [int(i) for i in input().split()]
d1, d2 = [int(i) for i in input().split()]

x = int((d1 - r2 + c1) / 2)
y = int(r1 - x)
z = int(d2 - y)
w = int(c2 - y)

possible = True

for i in [x, y, z, w]:
    if i <= 0 or i > 9:
        possible = False

if len([x, y, z, w]) != len(set([x, y, z, w])):
    possible = False

if possible:
    print(f'{x} {y}\n{z} {w}')
else:
    print(-1)
