import math
t = int(input())
for x in range(t):
    a, b = [int(i) for i in input().split()]
    emeralds = 0
    while a > 0 and b > 0:
        if a == b:
            emeralds += math.floor((a * (2/3)))
            break
        elif a > b:
            v = min(a - b, b)
            a -= (v * 2)
            b -= v
            emeralds += v
        else:
            v = min(b - a, a)
            a -= v
            b -= (v * 2)
            emeralds += v
    print(emeralds)
