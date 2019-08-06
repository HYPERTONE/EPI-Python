
# Write a program which takes as input a valid Roman number string s and returns the integer it corresponds to.

romanTable = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

# I can precede V and X
# X can precede L and C
# C can precede D and M

def roman(s):
    
    value = 0
    for i in range(0, len(s) - 1):                         # len(s) = 3, but we want purposely make it 2 (i = 0, 1)
        print(i)
        if romanTable[s[i]] < romanTable[s[i + 1]]:        # if 10 < 50
            value -= romanTable[s[i]]
            print(value)
        else:
            value += romanTable[s[i]]
    
    return value + romanTable[s[-1]]
        

roman('XLI') # -> 41
