# The simplest data structure is the array, which is a contiguous block of memory. It is usually used to represent sequences.

# When working with arrays you should take advantage of the fact that you can operate efficiently on both ends. For this problem,
# we can partition the array into three subarrays: Even, Unclassified, and Odd, appearing in that order.

def evenOdd(A):
    nextEven, nextOdd = 0, len(A) - 1
    while nextEven < nextOdd:
        if A[nextEven] % 2 == 0:
            nextEven += 1
        else:
            A[nextEven], A[nextOdd] = A[nextOdd], A[nextEven]
            nextOdd -= 1
            
sample = [5, 6, 10, 5, 7, 1, 2]
evenOdd(sample)
print(sample) # -> [2, 6, 10, 7, 1, 5, 5]


# 5.1 The Dutch National Flag Problem

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


# 5.2 - Increment An Arbitrary-Precision Integer

# Write a program which takes an input of digits encoding a nonnegative decimal integer D and updates the array to
# represent the integer D + 1.

# For example, if D = [1, 2, 9] then we should update the array to [1, 3, 0]

def plusOne(A):
    
    s = [str(i) for i in A]         # Convert the integer to a string
    result = int("".join(s)) + 1    # Join the string to an int; add 1
    
    return result

def plusOne2(B):
    result = []
    for index, value in enumerate(B[::-1]):     # No conversion here, just inverse the list and multiply 
        result.append(value * 10 ** index)      # by its value and 10^index
    
    return sum(result) + 1

def plusOne3(C):
    result = int("".join(map(str, C)))          # Similar to plusOne, map the str function with the list and join the values
    
    return result + 1

# 5.3 - Multiply Two Arbitrary-Precision Integers

# Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays to represent integers,
# e.g., with one digit per array entry, with the most significant digit appearing first, and a negative leading digit denoting
# a negative integer. For example, [-7, 6, 1, 8] represents -7618.

# Write a program that takes two arrays representing integers, and returns an integer representing their product.

def multiplyArrays(A, B):
    
    
    resultA = int("".join(map(str, A)))
    resultB = int("".join(map(str, B)))
    
    return resultA * resultB

# It's kind of strange that the authors say not to 'reinvent the wheel' yet they essentially rewrite certain built in functions.


# 5.4 - Advancing Through An Array

# In a particular board game, a player has to try and advance through a sequence of positions. 
# Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move.

# You begin at the first position, and win by getting to the last position. For example, 
# let A = [3,3,1,0,2,0,1] represent the board game. The game can be won by the following sequence of advances: 
# take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from A[4] to A[6], which is the last position. 





# 5.5 - Delete Duplicates From A Sorted Array

# This problem is concerned with deleting repeated elements from a sorted array. 
# For example, for the array A = [2,3,5,5,7,11,11,11,13], then after deletion, the array is [2,3,5,7,11,13,0,0,0]. 
# After deleting repeated elements, there are 6 valid entries.

# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed 
# and the remaining elements have been shifted left to fill the emptied indices.

def delDupes(A):
    
    increment = 0
    duplicates = []
    for i, j in enumerate(A[:-1]):
        if A[i + 1] == j:
#             print('duplicate of {} at index {}'.format(j, i))
            duplicates.append(j)
    
    # Remove duplicates (using values, since index will shift list and distort indexes)
    for d in duplicates:
        A.remove(d)
        
    print(A)
           
        
# 5.6 - Buy And Sell A Stock Once

# Consider the sequence A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]. The maximum profit that can be made with one buy
# and one sell is 30 - buy at 260 and sell at 290.

# Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by 
# buying and selling one share of that stock.

def buy_and_sell_stock_once(prices):
    
    min_price_so_far = float('inf')
    max_profit = 0.0
    
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit_sell_today, max_profit)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
buy_and_sell_stock_once(A)


# This is an uglier solution with a worse runtime.
def buyStockOnce(A):
    
    price = []
    for i, j in enumerate(A):
        for x in A[i:]:
            print('{} - {} = {}'.format(x, j, x - j)) # Sell Price - Buy Price
            price.append(x - j)
            
    return max(price)
    

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
buyStockOnce(A)


# 5.7 - Buy And Sell A Stock Twice

# Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.
# The second buy must be made on another date after the first sale.

def buy_and_sell_stock_twice(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day.
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
buy_and_sell_stock_twice(A)

# 5.8 - Computing An Alternation

# Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the property
# that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...

def rearrange(A):
    
    for i, j in enumerate(A):
        A[i:i+2] = sorted(A[i:i+2], reverse= i % 2) # where 0 = False, 1 = True
        print(sorted(A[i:i+2], reverse=i%2))
    
    return A

A = [1, 2, 3, 4, 5, 6]
rearrange(A)

# i=0; A[0:2] = sorted(1,2 reverse=0) = [1,2] => A=[1,2,3,4,5,6]
# i=1; A[1:3] = sorted(2,3 reverse=1) = [3,2] => A=[1,3,2,4,5,6]
# i=2; A[2:4] = sorted(2,4 reverse=0) = [2,4] => A=[1,3,2,4,5,6]
# i=3; A[3:5] = sorted(4,5 reverse=1) = [5,4] => A=[1,3,2,5,4,6]
# i=4; A[4:6] = sorted(4,6 reverse=0) = [4,6] => A=[1,3,2,5,4,6]
# i=5; A[5:7] = sorted(6 reverse=1) = [6] => A=[1,3,2,5,4,6]


# 5.9 - Enumerate All Primes to n

# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.

# Write a program that takes an integer argument and returns all the primes between 1 and that integer. For example,
# if the input is 18, you should return [2, 3, 5, 7, 13, 17]

def primes(n):

    checks = []
    primes = []
    for i in range(2, n):
        for j in [2, 3, 5, 7]:
            mod = i % j
            if i == j:
                pass
            else:
                checks.append(mod)

        if 0 not in checks:
            primes.append(i)

        checks = []

    return list(primes)
            
        
primes(18) --> [2, 3, 5, 7, 11, 13, 17]


# 5.10 - Permute The Elements Of An Array

# A permutation can be specified byh an array P, where P[i] represents the location of the element at i in the permutation.
# For example, the array [2, 0, 1, 3] represents the permutation that maps the element at location 0 to location 2, the 
# element at location 1 to location 0, the element at location 2 to location 1, and keep the element at location 3 unchanged.

# Given an array of n elements and a permutation P, apply P to A.

A = [0, 1, 2, 3, 4]
P = [4, 2, 3, 1, 0] # Positions
B = [4, 3, 2, 1, 0] # Positions 2

def permute(A, P):
    """Apply positions of A to P."""
    
    l = [0] * len(P)

    for index, value in enumerate(l):
        l[P[index]] = A[index]
    
    return l
    
permute(A, P) -> [4, 3, 1, 2, 0]
