# beats 91% - 68 ms
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity

        self.head = Node(-1, -1)
        self.end = Node(-1, -1)

        self.head.next = self.end
        self.end.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_position(node)
        return node.val

    def update_position(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

        tmp = self.head.next
        node.next = tmp
        tmp.prev = node

        node.prev = self.head
        self.head.next = node

    def add_node(self, node):
        tmp = self.head.next
        node.next = tmp
        tmp.prev = node
        self.head.next = node
        node.prev = self.head


    def delete_node(self, node):
        prv = node.prev
        prv.next = self.end
        self.end.prev = prv

        self.cache.pop(node.key)
        del prv


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update_position(node)
            return
        
        if len(self.cache) == self.size:
            node = self.end.prev
            self.delete_node(node)

        node = Node(key, value)
        self.add_node(node)
        self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
