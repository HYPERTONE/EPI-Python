
# Write a program which takes a non-negative integer and returns the largest integer whos square is less than or equal to the given integer.
# For example, if the input is 16, return 4. If the input is 300, return 17 since 17^2 = 289 < 300 (18^2 = 324 > 300).


def sqrt(k):
    
    left = 0
    right = k
    
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left - 1

sqrt(300) # -> 17
