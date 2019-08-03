
# Often data is almost sorted - for example, a server receives timestamped stock quotes and earlier quotes may arrive slightly
# after later quotes because of differences in sever loads and network routes.

# Write a program which takes as input a very long sequence of numbersd and prints the numbers in sorted order.
# Each number is at most k away from its correctly sorted position. For example, no number in the sequence <3,-1,2,6,4,5,8>
# is more than 2 away from its final sorted position.

import itertools

def sortApprox(sequence, k):
    result = []
    minHeap = []
    
    for x in itertools.islice(sequence, k):
        heapq.heappush(minHeap, x)
        
    for x in sequence:
        smallest = heapq.heappushpop(minHeap, x) # this pushes and pops the smallest element each time
        result.append(smallest) # and appends it to result (which sorts ascendingly)
        
    while minHeap:
        smallest = heapq.heappop(minHeap)
        result.append(smallest)
        
    return result
    
    
a = [3, -1, 2, 6, 4, 5, 8]
sortApprox(a, 2)
