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
        res = Node(0)
        dummy = res
        tmp = head
        reference_map = {}

        while tmp:
            curr = Node(tmp.val)
            reference_map[tmp] = curr
            dummy.next = curr
            dummy = dummy.next
            tmp = tmp.next

        tmp = head
        while tmp:
            node = reference_map[tmp]
            if tmp.random:
                random_node = reference_map[tmp.random]
                node.random = random_node
            tmp = tmp.next
        

        return res.next