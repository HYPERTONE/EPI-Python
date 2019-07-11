# A program updates variables in memory according to its instructions. 
# Variables come in types - a type is a classification of data that spells out possible values 
# for that type and the operations that can be performed on it. 
# In Python, everything is an object - this includes Booleans, integers, characters, etc.


# Count the number of bits that are set to 1 in an integer.
def countBits(x):
  numBits = 0
  
  while x:
    numBits += x & 1
    x >>= 1
  return numBits

countBits(42)
