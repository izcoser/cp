# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # not using strip() or split() for fair play
        s = s[::-1]
        count = 0
        for i in s:
            if i != ' ':
                count += 1
            elif count > 0:
                break
        return count