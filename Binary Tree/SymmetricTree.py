# Given a tree, check that it is symmetric
# The left child of the left subtree = right child of the right subtree AND
# The right child of the left subtree = left child of the right subtree


# Recursive solution
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right): # takes the left and right value
            if (left is None) or (right is None): # if either is null
                return left == right # we check that they're both null - they need to be equal/symmetric
            if left.val != right.val: # if they arent equal return False
                return False 
            return symmetric(left.left, right.right) and symmetric(left.right,right.left) # pass the combo because they both need to be true in order for the tree to be symmetric
        
        if root is None: # checking if root is null, we don't want to pass a null root to the function
            return True # would be true because a null root is "symmetric"
        
        return symmetric(root.left,root.right)


# Iterative solution
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right): # takes the left and right value
            if (left is None) or (right is None): # if either is null
                return left == right # we check that they're both null - they need to be equal/symmetric
            if left.val != right.val: # if they arent equal return False
                return False 
            return symmetric(left.left, right.right) and symmetric(left.right,right.left) # pass the combo because they both need to be true in order for the tree to be symmetric
        
        if root is None: # checking if root is null, we don't want to pass a null root to the function
            return True # would be true because a null root is "symmetric"
        
        return symmetric(root.left,root.right)
