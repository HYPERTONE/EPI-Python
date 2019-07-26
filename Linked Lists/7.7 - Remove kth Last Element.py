
# Given a singly linked list and an integer k, write a program to remove the kth last element from the list.
# You cannot assume that it is possible to record the length of the list.

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

def removeKth(L, k):
    dummy = ListNode(0, L)
    first = dummy.next
    
    for i in range(k):
        first = first.next
    print('first: {}'.format(first.data))
    
    second = dummy
    while first:
        first = first.next
        second = second.next
        # second points to the (k + 1)th last node, deletes its successor
        second.next = second.next.next
    return dummy.next

def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the k + 1 th last node, deletes successor
    second.next = second.next.next
    return dummy_head.next

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

NodePrint(a) # -> 1 2 3 4
