
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
