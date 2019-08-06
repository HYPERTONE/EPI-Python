
# Considering the following two rules that are to be applied to an array of characters:
# 1. Replace each 'a' by two 'd's
# 2. Delete each entry containing a 'b'

# Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a' by two 'd's. Along with the
# array, you are provided an integer-valued size. Size denotes the number of entries of the array that the operation is to be
# applied to. You do not have to worry about preserving subsequent entries.

# For example, if the array is [a, b, a, c, _] and the size is 4, you can return [d, d, d, d, c].

def replaceRemove(a, size):
    
    aEnhanced = []
    for i, j in enumerate(a):
        if j == 'a':
            for k in range(2):
                aEnhanced.append('d')
        elif j == 'b':
            pass
        else:
            aEnhanced.append(j)
    return aEnhanced[:size]

arr = ['a', 'b', 'c', 'a', 'd']
replaceRemove(arr, 4) # -> ['d', 'd', 'c', 'd']
