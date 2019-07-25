
# Write a program which takes a singly linked List L and two integers s and f as arguments, and reverses the order of the nodes 
# from the sth node to the fth node, inclusive. The numbering begins at 1, i.e. the head node is the first node.

# 11 -> 3 -> 5 -> 7 -> 2

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

#
def reverse_sublist(L, start, finish):
    # Make a dummy to return dummy.next -> 0, nextnode = L
    dummy_head = sublist_head = ListNode(0, L)

    for i in range(1, start):
        sublist_head = sublist_head.next
        
    # reverse
    sublist_iter = sublist_head.next
    for i in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
        
    return dummy_head.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

insertAfter(a, b)
insertAfter(b, c)
insertAfter(c, d) 
insertAfter(d, e) 
insertAfter(e, f) 
insertAfter(f,g)
# printNode(a)

z = reverse_sublist(a, 1, 7)
printNode(z)
