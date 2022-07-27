# This is my original solution which is unfortunately very slow but passes all the test cases.
# The optimal solution for this problem uses an Array so navigate to the array section to find it.

class Node:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.next = None

class MyHashMap:

    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        newnode = Node(key,value)
        if not self.head:
            self.head = newnode
        else:
            cur = self.head
            while cur:
                
                if cur.key == key:
                    cur.value = value
                    break
                    
                if cur.next is None:
                    cur.next = newnode
                    
                cur = cur.next

    def get(self, key: int) -> int:
        if self.head:
            cur = self.head
            while cur:
                if cur.key == key:
                    return cur.value
                cur=cur.next
        return -1

    def remove(self, key: int) -> None:
        if self.head:
            cur = self.head
            prev = None

            if cur.key == key:
                self.head = cur.next
                cur = None
                return
            
            while cur:
                if cur.key == key:
                    break
                prev = cur
                cur=cur.next
                
            if cur:
                prev.next = cur.next
                cur = None
                return
            
        return
      
      
    
