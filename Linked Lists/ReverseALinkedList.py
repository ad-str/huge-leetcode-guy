from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''My attempt. Actually is the exact same as the solution.'''
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev