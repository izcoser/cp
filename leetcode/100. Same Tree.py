from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.left) and dfs(left.right, right.right)
        
        return dfs(p, q)