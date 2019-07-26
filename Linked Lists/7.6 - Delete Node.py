 
# Write a program which deletes a node in a singly linked list. The input node is guaranteed not to be the tail node.

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

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

NodePrint(a) # -> 1 2 3 4

deleteNode(c) # delete (3)
NodePrint(a) # -> 1 2 4
