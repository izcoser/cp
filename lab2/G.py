# G - Colin and Ryan 

import math
def divisors(n, r): # divs > r
    d = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)
            if n // i != i:
                d.append(n // i)
    return [i for i in sorted(d) if i > r]

N = int(input())

for i in range(N):
    C, R = [int(i) for i in input().split()]
    
    if C == R:
        print('Case #' + str(i + 1) + ': 0')
        continue

    ds = ' '.join([str(d) for d in divisors(C - R, R)])
    if len(ds) > 0:
        print('Case #' + str(i + 1) + ': ' + ds)
    else:
        print('Case #' + str(i + 1) + ':')
    