# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = [[root, 0]]
        while queue:
            node, current = queue.pop(0)
            if node:
                current += node.val
                if not node.right and not node.left and current == targetSum:
                    return True
                queue.append([node.left, current])
                queue.append([node.right, current])
        return False
