import sys

def antipal(s):
    return s != s[::-1]

line = input().strip()
m = 0
if antipal(line):
    print(len(line))
    exit()

for j in range(len(line) - 1, 1, -1):
    subs = [line[i : i + j] for i in range(len(line)) if i + j <= len(line)]
    for s in subs:
        if antipal(s):
            m = len(s)
            print(m)
            exit()

print(0)
