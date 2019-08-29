
# A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant big (LSB), 
# and the bit at the index 63 corresponding to the most significant bit (MSB). 
# Implement code that takes a 64-bit integer as input and swaps the bits at indices i and j.

def bitSwap(x, i, j):
  # Check to see if i and j are the same. If they are, then there is no reason to swap them.
  if (x >> i) & 1 != (x >> j) & 1:
    bit_mask = (1 << i) | (1 << j)
    x ^= bit_mask
    return x

bitSwap(73, 1, 6) # If x = 73, i (MSB) has index 1, and j (LSB) has index 6 --> Output is 1011 (11) with bitmask 1000010 (66)

# 73 -> 1001001 where index 1 is 1 and index 6 is 0
# 73 -> [1]0010[0]1 we want to swap [1,6] to get 0001011 (which yields 11)

# So we compute a bitmask by left shifting 1 by i,j and applying an OR
# Then we XOR the bitmask with x to obtain our result
