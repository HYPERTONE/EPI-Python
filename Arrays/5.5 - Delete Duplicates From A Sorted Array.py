
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
