# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node
# Medium
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}

#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

#Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if it's a left child, it will always point to right sibling.
        # if it's a right child, it will point to null if parent points to null.
        #                        it will point to parent.next.left otherwise.
        # if it's a root, it will point to null.
        if root == None or root.left == None:
            return root
        
        root.left.next = root.right
        if root.next == None:
            root.right.next = None
        else:
            root.right.next = root.next.left

        return Node(root.val, self.connect(root.left), self.connect(root.right), root.next)