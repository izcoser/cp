from typing import List
# matrix, easy
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # iterate over the inner matrix:
        n = len(grid) # square matrix

        max_local = [[0] * (n - 2) for i in range(n - 2)]
        
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                values_in_window = [grid[a + i][b + j] for a in range(-1, 2) for b in range(-1, 2)]
                max_local[i - 1][j -1] = max(values_in_window)

        return max_local