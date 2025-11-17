# LL, easy, iterative, recursive
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) in time, O(n) in memory.
        stack = []
        while head:
            stack.append(head)
            head = head.next

        if len(stack) == 0:
            return

        head = stack.pop()
        n = head
        while len(stack) > 0:
            n.next = stack.pop()
            n = n.next
        n.next = None
        return head
    
    def reverseListOptimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) in time, O(1) in memory.
        prev, curr = None, head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev

    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) in time, O(n) in memory.
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseListRec(head.next)
            head.next.next = head 

        head.next = None


        return new_head