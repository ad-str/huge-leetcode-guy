# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''My solution has a worst-case run time of 2n. It iterates through the linked list once to get
        the size then iterates again to find the (size - nth)th element'''
        curr = head
        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        delIdx = size - n

        if delIdx == 0:
            return head.next

        prev = head
        curr = head.next
        idx = 1
        while curr:
            if idx == delIdx:
                prev.next = curr.next
                return head
            
            idx += 1
            prev = curr
            curr = curr.next


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''This solution runs in linear time. It's clever. It uses a left pointer and a right pointer. it
        iterates the right pointer first to get an n gap between the two pointers then iterates both until
        the right one reaches the end. In which case, the left pointer is the element that should be removed'''
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
