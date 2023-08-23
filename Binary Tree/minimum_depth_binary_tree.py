# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node.left and not node.right:
                return 1
            
            left = dfs(node.left) if node.left else float('inf')
            right = dfs(node.right) if node.right else float('inf')

            return 1 + min(left, right)

        return dfs(root)

# brute force
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = [[root, 1]]
    res = float('inf')
    while queue:
        node, depth = queue.pop(0)
        if node:
            if not node.left and not node.right:
                res = min(res, depth)
            queue.append([node.left, depth + 1])
            queue.append([node.right, depth + 1])
    return res
