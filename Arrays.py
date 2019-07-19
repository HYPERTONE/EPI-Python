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

def plusOne(A):
    
    s = [str(i) for i in A]         # Convert the integer to a string
    result = int("".join(s)) + 1    # Join the string to an int; add 1
    
    return result

def plusOne2(B):
    result = []
    for index, value in enumerate(B[::-1]):     # No conversion here, just inverse the list and multiply 
        result.append(value * 10 ** index)      # by its value and 10^index
    
    return sum(result) + 1

def plusOne3(C):
    result = int("".join(map(str, C)))          # Similar to plusOne, map the str function with the list and join the values
    
    return result + 1

# 5.3 - Multiply Two Arbitrary-Precision Integers

# Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays to represent integers,
# e.g., with one digit per array entry, with the most significant digit appearing first, and a negative leading digit denoting
# a negative integer. For example, [-7, 6, 1, 8] represents -7618.

# Write a program that takes two arrays representing integers, and returns an integer representing their product.

def multiplyArrays(A, B):
    
    
    resultA = int("".join(map(str, A)))
    resultB = int("".join(map(str, B)))
    
    return resultA * resultB

# It's kind of strange that the authors say not to 'reinvent the wheel' yet they essentially rewrite certain built in functions.


# 5.4 - Advancing Through An Array

# In a particular board game, a player has to try and advance through a sequence of positions. 
# Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move.

# You begin at the first position, and win by getting to the last position. For example, 
# let A = [3,3,1,0,2,0,1] represent the board game. The game can be won by the following sequence of advances: 
# take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from A[4] to A[6], which is the last position. 





# 5.5 - Delete Duplicates From A Sorted Array

# This problem is concerned with deleting repeated elements from a sorted array. 
# For example, for the array A = [2,3,5,5,7,11,11,11,13], then after deletion, the array is [2,3,5,7,11,13,0,0,0]. 
# After deleting repeated elements, there are 6 valid entries.

# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed 
# and the remaining elements have been shifted left to fill the emptied indices.

def delDupes(A):
    
    increment = 0
    duplicates = []
    for i, j in enumerate(A[:-1]):
        if A[i + 1] == j:
#             print('duplicate of {} at index {}'.format(j, i))
            duplicates.append(j)
    
    # Remove duplicates (using values, since index will shift list and distort indexes)
    for d in duplicates:
        A.remove(d)
        
    print(A)
           
        
A = [2,3,5,5,7,11,11,11,13]
delDupes(A)
