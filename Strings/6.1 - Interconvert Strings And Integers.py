
# Implement an integer to string conversion function, and a string to integer conversion function. For example, if the input to the first
# function is the integer 314, it should return the string '314' and if the input to the second function is the string '314' it should
# return the integer 314.


# Int To String
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

# String To Int
def string2Int(s):
    
    stringy = list(s)
    
    result = 0
    for i in s:
        result = result*10 + ord(i) - ord('0') # if ord('3') = 51, and ord('0') = 48
                                                # then 51 - 48 = 3.
    
    
    return result

        
string2Int('314') # -> 314
