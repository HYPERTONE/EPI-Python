
# The simplest data structure is the array, which is a contiguous block of memory. It is usually used to represent sequences.

# When working with arrays you should take advantage of the fact that you can operate efficiently on both ends. For this problem,
# we can partition the array into three subarrays: Even, Unclassified, and Odd, appearing in that order.

def evenOdd(A):
    nextEven = 0
    nextOdd = len(A) - 1
    
    while nextEven < nextOdd:
        if A[nextEven] % 2 == 0:
            nextEven += 1
        else:
            A[nextEven], A[nextOdd] = A[nextOdd], A[nextEven]
            nextOdd -= 1
            
sample = [5, 6, 10, 5, 7, 1, 2]
evenOdd(sample)
print(sample) # -> [2, 6, 10, 7, 1, 5, 5]
