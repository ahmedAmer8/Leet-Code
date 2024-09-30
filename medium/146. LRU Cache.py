class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def add(self, node):
        cur = self.tail.prev
        cur.next = node
        self.tail.prev = node
        node.prev = cur
        node.next = self.tail
        
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
