# H - Mere Array

import math

for i in range(int(input())):
    input()
    numbers = [int(i) for i in input().split()]
    s = sorted(numbers)
    m = min(numbers)
    possible = True
    for i in range(len(numbers)):
        if s[i] == numbers[i] or math.gcd(numbers[i], m) == m:
            continue
        else:
            possible = False
    
    if possible:
        print('YES')
    else:
        print('NO')