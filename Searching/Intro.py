
# Searching algorithms can be classified in a number of ways - is the underlying collection static or dynamic?


# Binary Search #

# Given an arbitrary collection of n keys, the only way to determine if a search key is present is by examining each element.
# Binary search is a natural elimination-based strategy for searching a sorted array. The idea is to eliminate half the keys from 
# consideration by keeping the keys in sorted order. If the search key is not equal to the middle element of the array, one of the two sets 
# of keys to the left and to the right of the middle element can be eliminated from further consideration.


# Searching Boot Camp

# Bisect Module
import bisect

# The purpose of Bisect is to find a position in a list where an element needs to be inserted to keep the list sorted.

l = [1, 3, 4, 4, 4, 6, 7]

# bisect(list, num, beginning, end) -> returns the position in a sorted list where the number passed in the argument can be 
# placed so as to maintain the sorted order.

print(bisect.bisect(l, 3)) 
print(bisect.bisect_left(l, 2)) # Index to the left
print(bisect.bisect_right(l, 2)) # Index to the right

# bisect.insort(list, num, beginning, end) -> returns sorted list after inserting number in appropriate position

bisect.insort(l, 2)
print(l) # -> [1, 2, 3, 4, 4, 4, 6, 7]

bisect.insort_left(l, 5)
print(l) # -> [1, 3, 4, 4, 4, 5, 6, 7]

bisect.insort_right(l, 8)
print(l) # -> [1, 3, 4, 4, 4, 6, 7, 8]
