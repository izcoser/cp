for i in range(int(input())):
    n = int(input())
    collections = []
    all_stamps = set()
    for j in range(n):
        xs = [int(i) for i in input().split()]
        m = xs[0]
        stamps = set(xs[1:])
        collections.append(stamps)
        all_stamps = all_stamps.union(stamps)

    unique_collections = []
    for idc, c in enumerate(collections):
        s = c
        for idk, k in enumerate(collections):
            if idc != idk:
                s = s - k
        unique_collections.append(s)

    all_unique = unique_collections[0]
    for c in unique_collections[1:]:
        all_unique = all_unique.union(c)

    distribution = [len(s) / len(all_unique) for s in unique_collections]
    print('Case ' + str(i + 1) + ': ' + ' '.join([f"{d*100:.6f}%" for d in distribution]))