"""
Given the root of a binary tree, 
display the node values at each level. 
Node values for all levels should be displayed on separate lines.
"""

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = self.right = None

def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)

def main():
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(35)

    bfs(root)

main()