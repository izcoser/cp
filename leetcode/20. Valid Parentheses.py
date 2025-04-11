# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != matches[i]:
                return False
        return len(stack) == 0