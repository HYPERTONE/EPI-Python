
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



class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
    
def searchList(L, key):
    while L and L.data != key:
        L = L.next
    # If key was not present in the list, L will have become null
    return L

# Insert new_node after node
def insertAfter(node, new_node):
    new_node.next = node.next
    node.next = new_node

# Delete a node
def deleteAfter(node):
    node.next = node.next.next

# Print
def printNode(node):
    temp = node
    print(temp.data)
    while temp.next:
        temp = temp.next
        print(temp.data)
        
# Merge 
def merge(L1, L2):
    # Dummy placeholder for the result
    dummyHead = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummyHead.next


    

x = ListNode(1)
xPrime = ListNode(4)
y = ListNode(3)

insertAfter(x, xPrime)

# printNode(x) # so now, our output will be 1, 4 

z = merge(x, y) # we merge 1, 4 with 3
printNode(x) # our output is 1, 3, 4
