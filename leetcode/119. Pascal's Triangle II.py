from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [1]
        for _ in range(0, rowIndex):
            innerRow = []
            above = out
            for j in range(len(above) - 1):
                innerRow.append(above[j] + above[j + 1])
            out = [1] + innerRow + [1]

        return out


