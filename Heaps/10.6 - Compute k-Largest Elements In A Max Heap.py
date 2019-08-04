
# A heap contains limited information about the ordering of elements.

# Given a max-heap, represented as an array A, design an algorithm that computes the k largest elements stored in the max-heap.
# You cannot modify the heap. 

# For example <561,314,401,28,156,359,271,11,3> the four largest elements are 561, 314, 401, 359.


import heapq

def kLargest(A, k):
    
    heapq.heapify(A)
    
    return heapq.nlargest(k, A)
    
A = [561, 314, 401, 28, 156, 359, 271, 11, 3]
kLargest(A, 4) # -> [561, 401, 359, 314]
