line = input().strip()
lookFor = {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
i = 0
for c in line:
    if c == lookFor[i]:
        i += 1
    if i == 5:
        print('YES')
        exit(0)

print('NO')
