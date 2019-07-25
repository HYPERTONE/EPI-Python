# A list implements an ordered collection of values, which may include reptitions. Specifically, a singly linked list is a data 
# structure that contains a sequence of nodes such that each node contains an object and a reference to the next node in the list.

# The first node is referred to as the head and the last node is referred to as the tail; the tail's next field is null.

# In a Double Linked List, each node has a link to its predecessor, similarily, a sentinel node or a self-loop can be used instead of null
# to mark the end of the list.

# A list is similar to an array in that it contains objects in linear order. The key difference are that inserting and deleting elements
# in a list has time complexity O(1). On the other hand, obtaining the kth element in a list is expensive, having O(n) time complexity.
# Lists are usually building blocks of more complex data structures.

# There are two tpyes of list-related problems - those where you have to implement your own list, and those where you have to exploit
# the standard list library.



# 7.1 - Merge Two Sorted Lists

# Consider two single linked lists in which each node holds a number. Assume the lists are sorted, i.e., numbers in the lists appear
# in ascending order within each list. The merge of the two lists is a list consisting of the nodes of the two lists in which numbers 
# appear in ascending order.

# Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field your program can change in a node 
# is its next field.




