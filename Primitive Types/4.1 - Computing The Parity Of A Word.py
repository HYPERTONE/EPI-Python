
# Parity checks are used to detect single bit errors in data storage & communication.
# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise it is 0.

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
