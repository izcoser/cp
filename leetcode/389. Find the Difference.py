# easy, sorting
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)

        len_a = len(a)
        i = 0
        while i < len_a and a[i] == b[i]:
            i +=1
        return b[i]