import sys
from math import exp, sin, cos, tan

p, q, r, s, t, u = 0, 0, 0, 0, 0, 0

def f(x):
    return p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x * x + u;

def bisection():
    lo = 0
    hi = 1
    while lo + 1e-8 < hi:
        m = (lo + hi) / 2
        if f(lo) * f(m) <= 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2

for line in sys.stdin:
    p, q, r, s, t, u = [int(i) for i in line.split()]
    if f(0) * f(1) > 0:
        print('No solution')
    else:
        print(f'{bisection():.4f}')
