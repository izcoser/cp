from typing import List
# medium, matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for i in rows_to_zero:
            for j in range(n):
                matrix[i][j] = 0
        
        for i in range(m):
            for j in cols_to_zero:
                matrix[i][j] = 0