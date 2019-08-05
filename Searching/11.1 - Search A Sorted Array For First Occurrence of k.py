
# Binary search commonly asks for the index of any element of a sorted array that is equal to a specified element.

# Write a method that takes a sorted array and a key and returns the index of the first occurrence of that key in the array. 
# For example, given <-14, -10, 2, 108, 108, 243, 285, 285, 285, 401> the method should return 3 when given key 108 and 6 when given key 285.


# Naive Approach (have to check each element)

def firstOccurrence(A, k):
    
    found = -1
    for i, j in enumerate(A):
        if j == k:
            found = i
            break
            
    return found


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
firstOccurrence(A, 108)



# Binary Approach (cut stuff in half)

def firstOccurrence(A, k):
    
    left = 0
    right = len(A) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if k < A[mid]:
            right = mid - 1
        elif k == A[mid]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return result
        
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
firstOccurrence(A, 285)
