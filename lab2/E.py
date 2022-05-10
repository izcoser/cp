while True:
    n = int(input())
    if n == 0:
        break
    cards = list(reversed(list(range(1, n + 1))))
    discarded = []
    while(len(cards) >= 2):
        discarded.append(cards.pop())
        cards = [cards[-1]] + cards[:-1]

    if len(discarded) > 0:
        print('Discarded cards: ' + ', '.join([str(d) for d in discarded]))
    else:
        print('Discarded cards:')
    print('Remaining card: ' + str(cards[0]))

