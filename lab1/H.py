while True:
    try:
        N, a, b = [int(i) for i in input().split()]
    except Exception as ex:
        break
    
    currentSoldier = 0
    dead = 0
    soldierToCount = {}

    while 1:
        nextSoldier = (a * (currentSoldier * currentSoldier) + b) % N
        if nextSoldier not in soldierToCount:
            soldierToCount[nextSoldier] = 1
        else:
            soldierToCount[nextSoldier] += 1

        if soldierToCount[nextSoldier] == 2:
            dead += 1
        elif soldierToCount[nextSoldier] == 3:
            break
        
        currentSoldier = nextSoldier
    
    print(N - dead)