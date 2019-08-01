
# A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is a mirror image of the
# right subtree.

# Write a prgoram that checks whether a binary tree is symmetric.

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

lefty = BinaryTreeNode(15, left=lefty1, right=None)
lefty1 = BinaryTreeNode(10)
righty = BinaryTreeNode(15, left=None, right=righty1)
righty1 = BinaryTreeNode(10)
root = BinaryTreeNode(0, lefty, righty)



def symmetric(tree):
    def checkSymmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data 
                    and checkSymmetric(subtree_0.left, subtree_1.right)
                    and checkSymmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not    
        return False
    return not tree or checkSymmetric(tree.left, tree.right)

        
        
symmetric(root) # -> True
