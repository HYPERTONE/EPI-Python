# The simplest data structure is the array, which is a contiguous block of memory. It is usually used to represent sequences.

# When working with arrays you should take advantage of the fact that you can operate efficiently on both ends. For this problem,
# we can partition the array into three subarrays: Even, Unclassified, and Odd, appearing in that order.

def evenOdd(A):
    nextEven, nextOdd = 0, len(A) - 1
    while nextEven < nextOdd:
        if A[nextEven] % 2 == 0:
            nextEven += 1
        else:
            A[nextEven], A[nextOdd] = A[nextOdd], A[nextEven]
            nextOdd -= 1
            
sample = [5, 6, 10, 5, 7, 1, 2]
evenOdd(sample)
print(sample) # -> [2, 6, 10, 7, 1, 5, 5]


# 5.1 The Dutch National Flag Problem

# Write a program that takes an array A and an index i into A, and rearranges the elements such that all elements
# less than A[i] (the 'pivot') appear first, followed by elements equal to the pivot, followed by elements greater
# than the pivot.

def Flag(A, ind):
    
    pivot = A[ind]
    s = []
    
    for key, value in enumerate(A):
        if value < pivot:
            s.insert(0, value)      # insert instead of append here to keep the list ordered,
        elif value == pivot:        # this way we keep pushing values from the front of the list (which is frowned upon)
            s.append(value)
    for key, value in enumerate(A):
        if value > pivot:
            s.append(value)
            
    print(pivot)
    print(s)
    
A = [0, 0, 3, 2, 0, 1, 4]
B = [0, 1, 2, 0, 2, 1, 1]
C = [9, 3, 1, 6, 3, 2, 3, 6, 9, 4]

# Flag(B, 1) -> [0, 0, 1, 1, 1, 2, 2]


# 5.2 - Increment An Arbitrary-Precision Integer

# Write a program which takes an input of digits encoding a nonnegative decimal integer D and updates the array to
# represent the integer D + 1.

# For example, if D = [1, 2, 9] then we should update the array to [1, 3, 0]
