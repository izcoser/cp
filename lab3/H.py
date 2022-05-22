# H - Football
import sys

goals = sys.stdin.read().splitlines()[1:]
teams = set(goals)
if len(teams) == 1:
    print(list(teams)[0])
    exit()

a, b = list(teams)
print(a if goals.count(a) > goals.count(b) else b)
