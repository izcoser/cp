# https://leetcode.com/problems/longest-palindromic-substring/description/

def expand(s: str, l: int, r: int) -> str:
    longest = ""
    while l >= 0 and r < len(s):
        if s[l] == s[r]:
            longest = s[l:r + 1]
            l -= 1
            r += 1
        else:
            break
    return longest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for idx, x in enumerate(s):
            p1 = expand(s, idx, idx + 1)
            p2 = expand(s, idx, idx)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest 