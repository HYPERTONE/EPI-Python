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


