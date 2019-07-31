
# A binary tree is said to be height balanced if for each node in the tree, the difference in height of its left and right subtrees
# is at most one. A perfect binary tree is height-balanced, as is a complete binary tree. A height-balanced binary tree does not have to 
# be perfect or complete.

# Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.

import collections

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

lefty = BinaryTreeNode(10)
righty = BinaryTreeNode(20)
root = BinaryTreeNode(0, leftBaby, rightBaby)


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )
    # first value of return indicates if balanced and if so
    # the second value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced
