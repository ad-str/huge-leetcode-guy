class LRUCache:

    def __init__(self, capacity: int):
        dummy = Node(-1)
        cur = dummy
        while capacity > 0:
            cur.next = Node(-1)
            cur = cur.next
            capacity -= 1
        self.head = dummy.next
        self.tail = self.head
        self.map = {}
        

    def get(self, key: int) -> int:
        return self.map[key].val if self.map[key] else -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.tail.next:
                self.tail.val = value
            else:
                self.head = self.head.next
                self.tail.next = Node(value)
            self.map[key] = self.tail
            self.tail = self.tail.next
        else:
            self.map[key].val = value



class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
