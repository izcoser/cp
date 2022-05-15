# J - Just Next !!!
for i in range(int(input())):
    n = int(input())
    ns = [int(x) for x in input().split()]

    j = n - 1
    while j != 0:
        if ns[j] > ns[j - 1]:
            
            k = j
            while k < n:
                if ns[k] <= ns[j - 1]:
                    break
                k += 1

            ns[j - 1], ns[k - 1] = ns[k - 1], ns[j - 1]

            ns = ns[:j] + sorted(ns[j:])         
            
            break
        j -= 1
    
    if j == 0:
        print(-1)
    else:
        print(''.join([str(i) for i in ns]))