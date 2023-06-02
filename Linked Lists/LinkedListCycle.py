# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''My solution takes O(n) space.'''
        nodeSet = set()

        curr = head
        while curr:
            if curr in nodeSet:
                return True
            else:
                nodeSet.add(curr)
            curr = curr.next
        
        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        '''O(1) space solution'''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
