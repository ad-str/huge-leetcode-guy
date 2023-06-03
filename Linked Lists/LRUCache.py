'''My orginial solution uses a doubly linked list but I couldn't debug in time.'''

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        dummy = Node(-1)
        cur = dummy
        while capacity > 0:
            cur.next = Node(-1)
            cur.next.prev = cur
            cur = cur.next
            capacity -= 1
        self.head = dummy.next
        self.tail = dummy
        self.map = {}
        

    def get(self, key: int) -> int:
        if self.map[key]:
            self.update(self.map[key])
            return self.map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.tail.next:
                self.tail.next.val = value
            else:
                self.head = self.head.next
                self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.map[key] = self.tail
        else:
            self.map[key].val = value
            self.update(map[key])

    def update(self, node: Node) -> None:
        if node is self.head:
            self.head = self.head.next
        else: 
            node.prev.next = node.next

        node.next = self.tail.next
        self.tail.next = node
        self.tail = node
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



'''Here is a much more clean solution. Node the insert and remove helper functions. Instead of a
dedicated update function, it just removes the node then inserts it again. Also, it uses a left and
right points like my head and tail but they are dummy nodes representing the two boundaries. It also
does not create placeholder nodes based on capacity which I did but I ended up treating them like they
weren't there anyway which was inefficient of me. It seems like the capacity is more of a red herring
in this problem because you aren't really initializng that many nodes it's more like just the limit.
Once the length of the map reaches the capacity, then you delete the leftmost node.'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
