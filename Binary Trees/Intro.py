
# A binary tree is either empty, or a root node r together with a left binary tree and a right binary tree. The subtrees themselves
# are binary trees. The left binary tree is referred to as the left subtree of the root, and the right is the right subtree of the root.

# Binary trees most commonly occur in the context of binary searches, wherein keys are stored in a sorted fashion. Binary trees are
# appropriate when dealing with hierarchies.

# For any node there exists a unique sequence of nodes from the root to that node with each node in the sequence being a child of the
# previous node. This sequence is referred to as the search path from the root to the node.

# A node is an ancestor of d if it lies on the search path from the root to do. If a node is an ancestor, we say d is a descendant of that node.

# The depth of a node n is the number of nodes on the search path from the root to n, not including n itself.

# The height of a binary tree is the maximum depth of any node in that tree.

# A level of a tree is all nodes at the same depth.

A full binary tree is a binary tree in which every node other than the leaves has two children. 

A perfect binary tree is a full binary tree in which all leaves are at the same depth, and in which every parent has two children. A
perfect binary tree of height h contains exactly 2^(h+1) - 1 nodes, of which 2^h are leaves.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left
as possible. A complete binary tree of n nodes has height [log n].

A key computation on a binary tree is traversing all the nodes in the tree. (Traversing is also called walking.)

