
# The problem is concerned with removing duplicates from a sorted list of integers.

# Write a program that takes as input a singly linked list of integers in sorted order, and removes duplicates from it. The list
# should be sorted.

class ListNode:
    def __init__(self, data=0, next_node=None):
            self.data = data
            self.next = next_node

def NodePrint(node):
    temp = node
    while temp.next:
        print(temp.data)
        temp = temp.next
        
            
def insertAfter(node, new_node):
    new_node.next = node.next
    node.next = new_node
    
    
def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next
    
def merge(L1, L2):
    dummy = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
    tail.next = L1 or L2
    return dummy.next

def removeDuplicates(L):
    it = L
    while it:
        # Uses next_distinct to find the next distinct value
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(1, c)
a = ListNode(1, b)

NodePrint(a) # -> 1 1 3 4

removeDuplicates(a) # -> 1 3 4
