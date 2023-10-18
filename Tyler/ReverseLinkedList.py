from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        out = []
        cur = self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return ' -> '.join(out)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            tmp = cur.next # store the next node
            cur.next = prev # reversing the arrow to point to previous node
            prev = cur # increment previous 
            cur = tmp # increment current from the temporary node we store
        return prev


if __name__ == "__main__":
    head = ListNode(val = 1, next = None)
    head.next = ListNode(val = 2, next = None)
    head.next.next = ListNode(val=3, next=None)
    head.next.next.next = ListNode(val=4, next=None)
    
    print(head)

    s = Solution()
    print(s.reverseList(head))
