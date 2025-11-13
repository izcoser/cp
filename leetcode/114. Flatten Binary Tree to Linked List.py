from typing import Optional
# Couldn't come up with a O(1) space solution yet.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            self.nodes.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        if not root:
            return

        for i in range(len(self.nodes) - 1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i + 1]
        
        self.nodes[len(self.nodes) - 1].left = None
        self.nodes[len(self.nodes) - 1].right = None

        