from typing import List
# matrix, easy
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        out = [[0] * m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                out[j][i] = matrix[i][j]
        
        return out