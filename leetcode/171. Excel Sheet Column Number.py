# easy
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        acc = 0
        for ida, a in enumerate(columnTitle[::-1]):
            acc += (ord(a) - ord('A') + 1) * 26 ** ida 
        return acc