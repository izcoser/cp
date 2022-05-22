# F - Make Them Odd

def choices(x):
    ch = []
    while x % 2 == 0:
        ch.append(x)
        x /= 2
    return ch

for i in range(int(input())):
    input()
    ns = map(int, input().split())
    ch = set()
    for j in ns:
            ch = ch.union(set(choices(j)))
    print(len(ch))


