# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''I tried making a priority queue that would contain the current heads of each linked list in
        sorted order then append the top element to the new list. However, this is O(kn) time since
        it takes k operations to add an element to the priority queue (worst case) and there are n nodes
        that would need to be added to the pq eventually. I should've realized it was merge sort by the
        description.'''
        pq = None

        while k > 0:
            for i in range(lists):
                node = lists[i]
                if node == None: continue

                lists[i] = lists[i].next
                node.next = None

                if pq == None:
                    pq = node
                else:
                    cur = pq
                    prev = None
                    while True:
                        if node.val < cur.val:
                            if prev:
                                prev.next = node
                            node.next = cur
                            break

                        if cur.next == None:
                            cur.next = node
                            break
                        
                        prev = cur
                        cur = cur.next
            
            top = pq
            pq = pq.next
            
                        
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        '''The solution basically does something similar to mergesort. It merges two lists at a time and
        then merges the remaining lists. Hence there are log(k) merges and each merge takes n time.'''
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


