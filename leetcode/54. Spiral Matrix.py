from typing import List
# matrix, medium
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        spiral = []

        direction = 'right'
        i = 0
        j = 0

        walked = 0
        walked_tiles = set()
        
        while walked != m * n:
            spiral.append(matrix[i][j])
            walked_tiles.add((i, j))
            walked += 1
            
            direction = calculate_next_direction(direction, i, j, m, n, walked_tiles)

            if direction == 'right':
                j += 1
            if direction == 'left':
                j -= 1
            if direction == 'down':
                i += 1
            if direction == 'up':
                i -= 1
            
        return spiral            

def calculate_next_direction(current_direction: str, i: int, j: int, m: int, n: int, walked_tiles: set[int, int]) -> str:
    if current_direction == 'right':
        if j < n - 1 and (i, j + 1) not in walked_tiles:
            return 'right'
        else:
            return 'down'

    if current_direction == 'down':
        if i < m - 1 and (i + 1, j) not in walked_tiles:
            return 'down'
        else:
            return 'left'

    if current_direction == 'left':
        if j > 0 and (i, j - 1) not in walked_tiles:
            return 'left'
        else:
            return 'up'
    
    if current_direction == 'up':
        if i > 0 and (i - 1, j) not in walked_tiles:
            return 'up'
        else:
            return 'right'