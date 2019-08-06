
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
