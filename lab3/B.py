import sys

d = {}
for line in sys.stdin:
    if ' ' in line:
        v, k = [a.strip() for a in line.split(' ')]
        d[k] = v

    elif line == '' or line == '\n':
        continue

    elif line.strip() in d:
        print(d[line.strip()])
    else:
        print("eh")