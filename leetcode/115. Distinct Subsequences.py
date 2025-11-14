# DP solution.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i: int, j: int):
            if len(s) - i < len(t) - j: # not enough characters
                return 0
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)

            else:
                cache[(i, j)] = dfs(i + 1, j)
        

# Non DP attempt, couldn't make it.

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         counter = 0
#         positions = set()

#         for i in range(1, len(t)):
#             part_one, part_two = t[:i], t[i:]

#             print(part_one, part_two)

#             j = 0
#             while j < len(s):
#                 part_one_found_at = s.find(part_one, j)

#                 print(f"searched for {part_one} in {s[j:]}")
#                 if part_one_found_at == -1:
#                     break

#                 k = part_one_found_at + len(part_one)
#                 while k < len(s):
#                     part_two_found_at = s.find(part_two, k)

#                     if part_two_found_at == -1:
#                         break
#                     pos = (part_one_found_at, part_two_found_at)
#                     if pos not in positions:
#                         print(pos)
#                         positions.add(pos)
#                         counter +=1

#                     k = part_two_found_at + len(part_two)

#                 j = part_one_found_at + len(part_one)

#         return counter
