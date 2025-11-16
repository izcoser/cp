from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.lst = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode]):
            if root == None:
                return
            
            dfs(root.left)
            self.lst.append(root.val)
            dfs(root.right)

        dfs(root)
        ret = self.lst
        self.lst = []
        return ret
        