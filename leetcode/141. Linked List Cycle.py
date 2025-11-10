from typing import Optional
# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# O(1) memory.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while True:
            if fast == slow:
                return True
            if fast == None:
                return False

            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False

            slow = slow.next