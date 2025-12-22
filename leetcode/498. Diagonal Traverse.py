from collections import defaultdict
from typing import List
# medium, matrix (direction based solution too confusing)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        res = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                res.extend(diagonals[d][::-1])
            else:
                res.extend(diagonals[d])
        
        return res