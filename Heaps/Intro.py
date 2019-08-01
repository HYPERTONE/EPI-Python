# A heap is a specialized binary tree - specifally a complete binary tree (meaning all levels are completely filled 
# except possibly the last level and the last level has all keys as left as possible).

# The keys must satisfy the heap property - the key at each node is at least as great
# as the keys stored at its children.

# A heap is sometimes referred to as a priority queue because it behaves like a queue, with one difference: each element has a 
# 'priority' associated with it, and deletion removes the element with the highest priority.

# Use a heap when all you care about is the largest or smallest elements, and you do not need to support fast lookup,
# delete, or search operations for arbitrary elements.

# A heap is a good choice when you need to compute the k largest or k smallest elements in a collection. For the former, 
# use a min-heap, for the latter use a max-heap.
