import sys

m = []
for line in sys.stdin:
    m.append([c for c in line.strip()])

for i in range(len(m) - 1):
    for j in range(len(m) - 1):
        l = [m[i][j], m[i + 1][j], m[i + 1][j+ 1], m[i][j+ 1]]
        a = l.count('#')
        b = l.count('.')
        if a >= 3 or b >= 3:
            print('YES')
            exit()
print('NO')
