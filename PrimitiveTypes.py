# A program updates variables in memory according to its instructions. 
# Variables come in types - a type is a classification of data that spells out possible values 
# for that type and the operations that can be performed on it. 
# In Python, everything is an object - this includes Booleans, integers, characters, etc.


# Count the number of bits that are set to 1 in an integer.
def countBits(x):
  numBits = 0
  
  while x:
    numBits += x & 1 # AND our input with 0001, then increase numBits by the result
    x >>= 1          # Shift our input one position to the right and repeat the process
  return numBits

countBits(42) #Yields an output of 3

# 42 -> 101010 AND 000001 yields 0, numBits = 0 + 0
#    -> 010101 AND 000001 yields 1, numbits = 0 + 1
#    -> 001010 AND 000001 yields 0, numbits = 1 + 0
#    -> 000101 AND 000001 yields 1, numbits = 1 + 1
#    -> 000010 AND 000001 yields 0, numbits = 2 + 0
#    -> 000001 AND 000001 yields 1, numbits = 2 + 1 = 3


# Parity checks are used to detect single bit errors in data storage & communication.
# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise it is 0.
# The following function uses brute force to determine the parity:

def parity(x):
  numBits = 0
  
  while x:
    numBits += x & 1 # AND our input with 0001, then increase numBits by the result
    x >>= 1          # Shift our input one position to the right and repeat the process
  
  if numBits % 2 == 0:
        return '{} -> {} -> Even'.format(x, numBits)
    else:
        return '{} -> {} -> Odd'.format(x, numBits)
 
parity(43) # 43 is 101011; Yields an output of '43 -> 4 -> Even'

# A better (faster) solution might be to use XOR
# If we had 32 bits, we can cut them in half and XOR them. This way we are essentially cutting them in half
# until we determine the parity at the least significant remnant.

# Say x = 15 (1111)
def qarity(x):
    x ^= x >> 32 # (1111 XOR 1111 >> 32 bits = 1111 XOR 0000, x = 15)
    x ^= x >> 16 # (1111 XOR 1111 >> 16 bits = 1111 XOR 0000, x = 15)
    x ^= x >> 8 # (1111 XOR 1111 >> 8 bits = 1111 XOR 0000, x = 15)
    x ^= x >> 4 # (1111 XOR 1111 >> 4 bits = 1111 XOR 0000, x = 15)
    x ^= x >> 2 # (1111 XOR 1111 >> 2 bits = 1111 XOR 0011, x = 12)
    x ^= x >> 1 # (1100 XOR 1100 >> 1 bit = 1100 XOR 0110, x = 10)
    print(x)
    
    return x & 0x1 # x = 10 which is 1010, 1010 AND 0001 = 0
  
  
# 4.2 Swap Bits

# A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant big (LSB), 
# and the bit at the index 63 corresponding to the most significant bit (MSB). 
# Implement code that takes a 64-bit integer as input and swaps the bits at indices i and j.

def bitSwap(x, i, j):
  # Check to see if i and j are the same. If they are, then there is no reason to swap them.
  if (x >> i) & 1 != (x >> j) & 1:
    bit_mask = (1 << i) | (1 << j)
    x ^= bit_mask
    return x

bitSwap(73, 1, 6) # If x = 73, i (MSB) has index 1, and j (LSB) has index 6 --> Output is 66

  # 73 -> 1001001 (Our goal is to swap index 1 and 6 which should give 0001011)
  # 1001001 >> 1 = 0100100 AND 01 = 0 [IS NOT EQUAL TO] 1001001 >> 6 = 0000001 AND 01 = 1 [TRUE - THEY ARE NOT EQUAL]
  # bit_mask = (01 << 1) | (01 << 6)
  # bit_mask = (0010) | (01000000)
  # bit_mask = 1000010 = 66
  # x XOR bit_mask = 1001001 XOR 001011 -> 0001011 = 11

  
# Reverse Bits
#Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting 
#of the bits of the input in reverse order.

def reverseBit(num):
    result = 0
    while num:
        result = (result << 1) + (num & 1)
        num >>= 1
    return result
# 
# The goal here is to AND our num by 1 and then have it shifted to the LEFT one place while
# num is being shifted to the RIGHT. Every time we AND something, we will get a 1 when num had a 1,
# and a 0 when num had a zero. The loop terminates because num gets shifted until it becomes 0.



# 4.5 Compute x*y without arithmetical operators

# Sometimes the processors used in ultra low-power devices such as hearing aids do not have dedicated hardware for performing
# multiplication. A program that needs to perform multiplication must do some explicitly using lower-level primitives.

# Write a program that multiplies two nonnegative integers. 

# To multiply x by y we initialize the result to 0 and iterate through the bits of x, adding 2^k*y to the result
# if the kth bit of x is . The value 2^k*y can be computed by left-shifting y by k.
 
# 9 = 1001 = x
# 5 = 0101 = y
# Result = 0
# Iterate x:
# 1st (LSB of x) = 1, R = 0101                2^0*y = 1 * y = 0101
# 2nd (0) = Do nothing                    
# 3rd (0) = Do nothing
# 4th (1) = left shift y by 3 => 0101000      2^3*y = 8 * y => 1000 * y => left shift y by 3 => 0101000
# R = 0101 + 0101000 = 0101101 = 45

def multiply(x, y):
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1,
                                          temp_b >> 1)
        print(running_sum | carryin)  
        return running_sum | carryin
    
    running_sum = 0
    while x:    # Examines each bit of x
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

