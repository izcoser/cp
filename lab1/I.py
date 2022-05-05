t = int(input())
for i in range(t):
    n, k = [int(i) for i in input().split()]

    a = k
    b = int(str(k * k)[:n])
    m = max(a, b)

    while(a != b):
        a = int(str(a * a)[:n])
        b = int(str(b * b)[:n])
        if max(a, b) > m:
            m = max(a, b)
        b = int(str(b * b)[:n])
        if max(a, b) > m:
            m = max(a, b)
    
    print(m)
