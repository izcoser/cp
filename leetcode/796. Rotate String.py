# string matching, easy
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            shifted = shift(s)
            if shifted == goal:
                return True
            s = shifted
        return False

def shift(s: str) -> str:
    if len(s) == 1:
        return s
    return s[1:] + s[0]