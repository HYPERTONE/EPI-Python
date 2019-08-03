
# An array is said to be k-increasing-decreasing if elements repeatedly increase up to a certain index after which they decrease,
# then again increase, a total of k times.

# 57 131 493 294 221 339 418 452 442 190

# Design an efficient algorithm for sorting a k-increasing-decreasing array.

import heapq

def kIncDec(a):
    
    heapq.heapify(a)
    
    return heapq.nsmallest(len(a), a)
       
    
k = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]    
kIncDec(k) # -> [57, 131, 190, 221, 294, 339, 418, 442, 452, 493]
