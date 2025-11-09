# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = []
        for _ in range(numRows):
            rows.append([])

        currentRow = 0
        down = True
        for c in s:
            rows[currentRow].append(c)
  
            if currentRow == 0:
                down = True
            
            elif currentRow == numRows - 1:
                down = False

            currentRow += 1 if down else -1 
    
        out = ""
        for r in rows:
            out += ''.join(r)

        return out