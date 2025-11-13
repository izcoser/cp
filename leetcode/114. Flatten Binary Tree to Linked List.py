from typing import Optional
# Came up with an O(1) space solution later.

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

        
class SolutionO1Space:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # necessary?
        if not root.left and not root.right:
            return

        if root.left and not root.right:
            left_child = root.left
            root.left = None
            self.flatten(left_child)    
            root.right = left_child
        
        if root.right and not root.left:
            self.flatten(root.right)
            pass

        if root.right and root.left:
            left_child = root.left
            right_child = root.right

            root.right = left_child
            root.left = None

            self.flatten(left_child)
            n = left_child
            while n.right != None:
                n = n.right
            n.right = right_child
            self.flatten(right_child)

