from typing import Optional
'''My original implementation and it passes'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        head = head.next
        res.next = None

        while head:
            nxt = head.next
            if head.val < res.val:
                head.next = res
                res = head
            else:
                cur = res
                while cur.next and head.val > cur.next.val:
                    cur = cur.next
                head.next = cur.next
                cur.next = head
            head = nxt
        
        return res

'''My next implementation when I remembered about dummy heads'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-5000, next=head)
        head = head.next
        dummy.next.next = None

        while head:
            nxt = head.next
            cur = dummy
            while cur.next and head.val > cur.next.val:
                cur = cur.next
            head.next = cur.next
            cur.next = head
            head = nxt
        
        return dummy.next

'''For some reason my implementations are a little slow compared to others. Here is an implementation that is faster. Stared at it
for a while and can't understand what exactly the optimization is but has something to do with the last_sorted node.'''
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        # No need to sort for empty list or list of size 1
        if not head or not head.next:
            return head
        
        # Use dummy_head will help us to handle insertion before head easily
        dummy_head = ListNode(val=-5000, next=head)
        last_sorted = head # last node of the sorted part
        cur = head.next # cur is always the next node of last_sorted
        while cur:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # Search for the position to insert
                prev = dummy_head
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                # Insert
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = last_sorted.next
            
        return dummy_head.next