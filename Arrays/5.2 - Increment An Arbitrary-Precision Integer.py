
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
