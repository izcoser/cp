from typing import Optional
# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# O(1) memory.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        
        else:
            return None
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow