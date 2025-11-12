from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left_height = height(node.left)

            if left_height == -1:
                return -1
            
            right_height = height(node.right)
            if right_height == -1:
                return -1
            
            if abs(right_height - left_height) > 1:
                return -1
            
            return 1 + max(right_height, left_height)

        return height(root) != -1


# Works but messy.
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
        
#         height_left = height(root.left, 0)
#         height_right = height(root.right, 0)

#         print(height_left, height_right)

#         if height_right == -1 or height_left == -1:
#             return False

#         return abs(height_left - height_right) <= 1        


# def height(root: Optional[TreeNode], acc: int) -> int:
#     if not root:
#         return acc

#     if root.left and not root.right:
#         if root.left.left or root.left.right:
#             return -1
    
#     if root.right and not root.left:
#         if root.right.right or root.right.left:
#             return -1
    
#     height_left = height(root.left, acc + 1)
#     if height_left == -1:
#         return -1
    
#     height_right = height(root.right, acc + 1)
#     if height_right == -1:
#         return -1
    
#     if abs(height_left - height_right) > 1:
#         return -1

#     return max(height_left, height_right)

