# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''My first attempt. I tried to merge them by constantly swapping between the two lists. I should
        have just made a new linked list to append to.'''
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1.next
            list1.next = list2
            curr = list1.next
        else:
            head = list2.next
            list2.next = list1
            curr = list2.next

        headhead = head

        while curr.next:
            if curr.next.val < head.val:
                curr = curr.next
            else:
                temp = curr.next
                curr.next = head
                head = temp
                curr = curr.next
        
        curr.next = head

        return headhead

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''Solution. Makes a new list using a dummy node.'''
        dummy = ListNode()
        curr = dummy 

        while list1 and list2:
            if list1 < list2:
                curr.next = list1 
                list1 = list1.next
            else:
                curr.next = list2 
                list2 = list2.next 
            curr = curr.next
        
        if list1:
            curr.next = list1 
        elif list2:
            curr.next = list2 
        
        return dummy.next