
# Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting 
# of the bits of the input in reverse order.

def reverseBit(num):
    result = 0
    while num:
        result = (result << 1) + (num & 1)
        num >>= 1
    return result

# The goal here is to AND our num by 1 and then have it shifted to the LEFT one place while
# num is being shifted to the RIGHT. Every time we AND something, we will get a 1 when num had a 1,
# and a 0 when num had a zero. The loop terminates because num gets shifted until it becomes 0.


# Note that this is reversing the base 2 value of the integer. So if we input an integer of 123, its binary value is 1111011.
# The reverse of 1111011 is 1101111 which when converted to an integer is actually 111.
