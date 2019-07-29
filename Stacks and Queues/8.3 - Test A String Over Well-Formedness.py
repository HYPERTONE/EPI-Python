
# A string over the characters "{,},(,),[,]" is said to be well-formed if the different types of brackets match in the correct order.

# For example, "([]){()}" is well formed, as is "[()[]{()()}]". However, "{)" and "[()[]{()()" are not well-formed.

# Write a program that tests if a string made up of the characters '(',')','[',']','{', and '}' is well-formed.

def wellFormed(s):
    
    LOOKUP = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
             }
    
    leftChars = []
    for c in s:
        if c in LOOKUP:
            leftChars.append(c)
            print(leftChars)
        elif not leftChars or LOOKUP[leftChars.pop()] != c: # if leftChars is empty OR
            print('not found: {}'.format(leftChars)) # if a ( exists, we append it (since its in the lookup) and then we 
            return False                             # pop it and compare it to the previous stack item

    return not leftChars

wellFormed('{{(}}') # -> True
