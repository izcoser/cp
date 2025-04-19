# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth_recursive(node, cur_depth) -> int:
            if node == None:
                return cur_depth

            return max(max_depth_recursive(node.left, cur_depth + 1), max_depth_recursive(node.right, cur_depth + 1))

        return max_depth_recursive(root, 0)