# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution:
    def __init__(self):
        self.ps = []

    def generateParenthesis(self, n: int) -> List[str]:
        p = "("
        self.branch_from(p, n)
        return self.ps
        
        
    def branch_from(self, p, n):
        if len(p) == 2 * n:
            self.ps.append(p)
            return
        
        open = p.count("(")
        closed = p.count(")")

        if open < n:
            self.branch_from(p + "(", n)

        if closed < open:
            self.branch_from(p + ")", n)

a = Solution()
ps = a.generateParenthesis(3)
print(ps)