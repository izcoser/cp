from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertRecursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return root
                
            root.left, root.right = root.right, root.left
            
            invertRecursive(root.left)
            invertRecursive(root.right)

            return root
        
        invertRecursive(root)
        return root

        