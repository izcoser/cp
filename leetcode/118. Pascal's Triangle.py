from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(1, numRows):
            innerRow = []
            above = out[-1]
            for j in range(len(above) - 1):
                innerRow.append(above[j] + above[j + 1])
            out.append([1] + innerRow + [1])

        return out

