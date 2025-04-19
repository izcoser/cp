# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        nodes = []

        current = head
        while current != None:
            nodes.append(current)
            current = current.next
        
        nth_from_end = nodes[ - 1 * n]

        # get previous node if exists
        before_nth_from_end = nodes[ (- 1 * n) - 1] if abs((- 1 * n) - 1) <= len(nodes) else None 
        
        if before_nth_from_end:
            before_nth_from_end.next = nth_from_end.next
        else:
            # removing first node
            head = nodes[1]

        return head
        