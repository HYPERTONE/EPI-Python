
# Design an efficient algorithm that takes a sorted array of distinct integers, and returns an index i such that the 
# element at index i equals i.

# For example, if the input is <-2, 0, 2, 3, 6, 7, 9> your algorithm should return 2 or 3.

def entryIndex(A):
    
    left = 0
    right = len(A) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid + 1
            
    return result
            
A = [-2, 0, 2, 3, 6, 7, 9]
entryIndex(A) # -> 3
