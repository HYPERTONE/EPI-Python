
# A hash table is a data structure used to store keys, optionally with corresponding values.

# The underlying idea is to store keys in an array. A key is stored in the array locations ('slots') based on its 'hash code'. 
# The hash code is an integer computed from the key by a hash function. If the hash function is chosen well, the objects are distributed
# uniformly across the array locations.

# If two keys map to the same location, a 'collision' will occur. The standard mechanism to deal with collisions is to maintain a linked
# list of objects at each array location.

# A hash table is qualitatively different from a sorted array - keys do not have to appear in order, and randomization (specifically,
# the hash function) plays a central role. Compared to binary search trees, inserting and deleting in a hash table is more efficient.

# One disadvantage of hash tables is the need for a good hash function but this is rarely an issue in practice.

# A hash function has one hard requirement - equal keys should have equal hash codes.

# A softer requirement is that the hash function should 'spread' keys, i.e., the hash codes for a subset of objects should be uniformly
# distributed across the underlying array.

# A common mistake with hash tables is that a key that's present in a hash table will be updated. The consequence is that a lookup for 
# that key will now fail, even though its still in the hash table. If you have to update a key, first remove it, then update it, 
# and finally add it back - this ensures it's moved to the correct array location. 

# As a rule, you should avoid using mutable objects as keys.


# A hash table is a good data structure to represent a dictionary, i.e., a set of strings. 

Consider a class that represents contacts. Assume each contact is a string. Suppose that the individual contacts are to be stored in a 
list and it's possible that the list contains duplicates. Two contacts should be equal if they contain the same set of strings, 
regardless of the ordering of the strings within the underlying list. Multiplicity is not important, i.e., three repetitions of the 
same contact is the same as a single instance of that contact.

