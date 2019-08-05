
# An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it becomes sorted. For example,
# <378, 478, 550, 631, 103, 203, 220, 234, 279, 368> can be shifted to the left by 4 to become sorted.

def cyclically(A):
    
    left = 0
    right = len(A) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
            
    return left

A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
cyclically(A) # -> 4
