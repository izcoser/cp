n = int(input())
ns = sorted([int(i) for i in input().split()])
s = 0
notdisappointed = 0
for i in ns:
    if s <= i:
        notdisappointed += 1
        s += i
        
print(notdisappointed)