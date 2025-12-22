a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(a)):
    for j in range(len(a[0])):
        if i < j:
            a[i][j], a[j][i] = a[j][i], a[i][j]

for r in a:
    print(r)