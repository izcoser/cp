from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def get_path(root, s):
            if root.left == None and root.right == None:
                return paths.append(s + str(root.val))

            if root.left:
                get_path(root.left, s + str(root.val) + "->")

            if root.right:
                get_path(root.right, s + str(root.val) + "->")


        get_path(root, "")
        return paths
        