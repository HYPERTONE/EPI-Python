# Strings are ubiquitous in programming today - scripting, web development, and bioinformatics all make extensive use of strings.

# You should know how strings are represented in memory, and understand basic operations on strings such as comparison,
# copying, joining, splitting, matching, etc. Advanced string processing algorithms often use hash tables (Chapter 12) and
# dynamic programming (Page 234).

# A palindromic string is one which reads the same when it is reversed.


# 6.1 - Interconvert Strings And Integers


# Implement an integer to string conversion function, an da string to integer conversion function. For example, if the input to the first
# function is the integer 314, it should return the string '314' and if the input to the second function is the string '314' it should
# return the integer 314.



def int2String(x):
    
    negator = False
    if x < 0:
        negator = True
        
    values = []
    while True: 
        values.append(chr(ord('0') + x % 10)) # Modulo catches the remainder of each value 
        x //= 10                              # ord() converts a character to its unicode value; char() takes that unicode value and 
        if x == 0:                            # outputs its unicode character representation. 
            break                             # Floor division shifts the integer to the left so that we can catch the next value
        
    return "".join(values[::-1])
    
        
int2String(123) # -> '123' 

