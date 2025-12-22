from collections import defaultdict
from typing import List
# medium, matrix
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        res = []
        for d in sorted(diagonals):
            res.extend(reversed(diagonals[d]))

        return res
