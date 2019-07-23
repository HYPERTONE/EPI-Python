# Strings are ubiquitous in programming today - scripting, web development, and bioinformatics all make extensive use of strings.

# You should know how strings are represented in memory, and understand basic operations on strings such as comparison,
# copying, joining, splitting, matching, etc. Advanced string processing algorithms often use hash tables (Chapter 12) and
# dynamic programming (Page 234).

# A palindromic string is one which reads the same when it is reversed.


# 6.1 - Interconvert Strings And Integers


# Implement an integer to string conversion function, an da string to integer conversion function. For example, if the input to the first
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


# 6.2 - Base Conversion

# Write a program that performs base conversion. The input is a string, an integer b1, and another integer b2. The string
# represents an integer in base b1. The output should be the string representing the integer in base b2. 

# For example, if the string is '615', b1 is 7 and b2 is 13, then the result should be '1A7', 
# since 6 x 7^2 + 1 x 7 + 6 = 1 x 13^2 + 10 x 13 + 7.

import string
import functools

def convert_base(stringg, b1, b2):
    def construct(integer, base):
        return ('' if integer == 0 else
                construct(integer//base, base) +
                string.hexdigits[integer % base].upper())
    is_negative = (stringg[0] == '-')
    integer = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        stringg[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if integer == 0 else
                                           construct(integer, b2))

thestring = "615"
print(convert_base(thestring, 7, 13))


# 6.3 - Compute The Spreadsheet Column Encoding

# Implement a function that converts a spreadsheet column id to the corresponding integer, with "A" corresponding to 1.
# For example, you should return 4 for "D", 27 for "AA", 702 for "ZZ", etc.

alphabet = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# multiplier = math.ceil(702 / len(alphabet))

multiplier = 704

while multiplier > 26:
    multiplier = math.ceil(multiplier / 26)
    print(multiplier)
    if multiplier <= 26:
        break
