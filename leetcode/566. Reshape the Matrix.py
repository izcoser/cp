from typing import List
# matrix, easy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        out = [[0] * c for i in range(r)]
        flattened_mat = []
        for row in mat:
            flattened_mat += row
        
        k = 0
        for i in range(r):
            for j in range(c):
                out[i][j] = flattened_mat[k]
                k += 1
        
        return out