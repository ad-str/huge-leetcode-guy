"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''My solution. I got a little help with it. I got to a point where I was thinking of making a
        map that points from old nodes to new nodes but I wasn't sure that was the correct way to do it.
        When I started to look up the answer, they indeed said it would use a map so I stopped the video 
        and started coding up my solution.'''
        copyMap = {}

        curr = head
        while curr:
            new = Node(curr.val, None, None)
            copyMap[curr] = new
            curr = curr.next

        curr = head
        while curr:
            copy = copyMap[curr]
            copy.next = copyMap[curr.next] if curr.next else None
            copy.random = copyMap[curr.random] if curr.random else None
            curr = curr.next
        
        return copyMap[head] if head else None


    def copyRandomList2(self, head: "Node") -> "Node":
        '''This solution is a condensed version of my code. It hard codes None as a key in the map.'''
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
