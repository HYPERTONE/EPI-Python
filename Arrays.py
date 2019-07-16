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

def dutch(A, ind):
    new = []
    pivot = A[ind]
    for item in A:
        if item < pivot:
            print(item)
        
l = [0, 1, 2, 0, 2, 1, 1]
dutch(l, 4
