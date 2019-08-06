
# Imlement a function which takes as input a string s and returns true if s is a palindromic string.

# For example, "A man, a plan, a canal, Panama." and "Able was I, ere I saw Elba" are palindromic, but "Ray a Ray" is not.

def palindromitic(s):
    
    chars = [',', '.', '!', ' ']
    for c in chars:
        s = s.replace(c, '')
    
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False

    
palindromitic("A man, a plan, a canal, Panama.") # -> True
