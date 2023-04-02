class TreeNode:
    def __init__(self, val = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    bfs_queue = [[tree, 1]]
    res = 1
    while bfs_queue:
        node, dpth = bfs_queue.pop(0)
        if node:
            res = max(res, dpth)
            bfs_queue.append([node.left, dpth + 1])
            bfs_queue.append([node.right, dpth + 1])

    print(res)