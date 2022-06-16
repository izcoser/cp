import sys
import math
input()
for line in sys.stdin:
    n, k = [int(i) for i in line.split()]
    print(k + math.ceil(k / (n - 1)) - 1)
