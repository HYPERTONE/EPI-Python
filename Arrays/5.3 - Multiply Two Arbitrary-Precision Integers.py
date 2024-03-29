
# Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays to represent integers,
# e.g., with one digit per array entry, with the most significant digit appearing first, and a negative leading digit denoting
# a negative integer. For example, [-7, 6, 1, 8] represents -7618.

# Write a program that takes two arrays representing integers, and returns an integer representing their product.

def multiplyArrays(A, B):
    
    
    resultA = int("".join(map(str, A)))
    resultB = int("".join(map(str, B)))
    
    return resultA * resultB
