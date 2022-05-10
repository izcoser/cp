import sys

def jolly(numbers):
    differences = []
    prev = numbers[0]
    for i in numbers[1:]:
        differences.append(abs(i - prev))
        prev = i

    if sorted(differences) == list(range(1, len(numbers))):
        return True
    else:
        return False


for line in sys.stdin:
    if len(line) < 2:
        break
    numbers = [int(i) for i in line.split()]
    n = numbers[0]
    numbers = numbers[1:]

    if len(numbers) == 1:
        print("Jolly")
        continue

    else:
        if jolly(numbers):
            print("Jolly")
        else:
            print("Not jolly")

