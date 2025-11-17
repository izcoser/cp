# easy
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            columnNumber -= 1
            c = columnNumber % 26
            columnNumber //= 26
            out += chr(c + ord('A'))
        return out[::-1]
