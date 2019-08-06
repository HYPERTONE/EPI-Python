
# Given a string containing a set of words separated by whitespace, we would like to transform it to a string in which the words 
# appear in the reverse order. For example, "Alice likes Bob" transforms to "Bob likes Alice". We don't need to keep the original string.

# Implement a function for reversing the words in a string s.

def reverseString(s):
    
    newString = s[::-1].split(' ')
    
    f = ''
    for word in newString:
        f = f + word[::-1] + ' '
    
    print(f)
    
reverseString('ram is costly') # -> costly is ram
