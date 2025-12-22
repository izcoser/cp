from typing import List
# matrix, easy
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        out = []
        
        for i in range(n):
            row = []
            for j in range(n - 1, -1, -1):
                value = (image[i][j] + 1) % 2
                row.append(value)
            out.append(row)
        
        return out