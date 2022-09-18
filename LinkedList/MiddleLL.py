# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, fast = head, head
        
        while fast and fast.next:  
            cur = cur.next
            fast = fast.next.next
            
        return cur