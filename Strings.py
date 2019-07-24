# Strings are ubiquitous in programming today - scripting, web development, and bioinformatics all make extensive use of strings.

# You should know how strings are represented in memory, and understand basic operations on strings such as comparison,
# copying, joining, splitting, matching, etc. Advanced string processing algorithms often use hash tables (Chapter 12) and
# dynamic programming (Page 234).

# A palindromic string is one which reads the same when it is reversed.


# 6.1 - Interconvert Strings And Integers


# Implement an integer to string conversion function, an da string to integer conversion function. For example, if the input to the first
# function is the integer 314, it should return the string '314' and if the input to the second function is the string '314' it should
# return the integer 314.


# Int To String
def int2String(x):
    
    negator = False
    if x < 0:
        negator = True
        
    values = []
    while True: 
        values.append(chr(ord('0') + x % 10)) # Modulo catches the remainder of each value 
        x //= 10                              # ord() converts a character to its unicode value; char() takes that unicode value and 
        if x == 0:                            # outputs its unicode character representation. 
            break                             # Floor division shifts the integer to the left so that we can catch the next value
        
    return "".join(values[::-1])
    
        
int2String(123) # -> '123' 

# String To Int
def string2Int(s):
    
    stringy = list(s)
    
    result = 0
    for i in s:
        result = result*10 + ord(i) - ord('0') # if ord('3') = 51, and ord('0') = 48
                                                # then 51 - 48 = 3.
    
    
    return result

        
string2Int('314') # -> 314


# 6.2 - Base Conversion

# Write a program that performs base conversion. The input is a string, an integer b1, and another integer b2. The string
# represents an integer in base b1. The output should be the string representing the integer in base b2. 

# For example, if the string is '615', b1 is 7 and b2 is 13, then the result should be '1A7', 
# since 6 x 7^2 + 1 x 7 + 6 = 1 x 13^2 + 10 x 13 + 7.

import string
import functools

def convert_base(stringg, b1, b2):
    def construct(integer, base):
        return ('' if integer == 0 else
                construct(integer//base, base) +
                string.hexdigits[integer % base].upper())
    is_negative = (stringg[0] == '-')
    integer = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        stringg[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if integer == 0 else
                                           construct(integer, b2))

thestring = "615"
print(convert_base(thestring, 7, 13))


# 6.3 - Compute The Spreadsheet Column Encoding

# Implement a function that converts a spreadsheet column id to the corresponding integer, with "A" corresponding to 1.
# For example, you should return 4 for "D", 27 for "AA", 702 for "ZZ", etc.

def intSpreadsheet(colNum):
    s = ""
    
    while colNum > 0:                               # 
        colNum, remainder = divmod(colNum - 1, 26)  # x = num - 1, y = 26; colNum = quotient, remainder = remainder
        s = chr(65 + remainder) + s                 # 65 = A, 66 = B, etc.
    return s

intSpreadsheet(702) # -> 'ZZ'

# For 702, we divmod(701, 26) which results in quotient = 26 with remainder = 25. Second iteration results in
# divmod(25, 26) which results in quotient = 0 with remainder = 25. After 2 iterations s = 'ZZ'
# chr(65) = 'A' + 25 gives chr(90) = 'Z'


# 6.4 - Replace & Remove

# Considering the following two rules that are to be applied to an array of characters:
# 1. Replace each 'a' by two 'd's
# 2. Delete each entry containing a 'b'

# Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a' by two 'd's. Along with the
# array, you are provided an integer-valued size. Size denotes the number of entries of the array that the operation is to be
# applied to. You do not have to worry about preserving subsequent entries.

# For example, if the array is [a, b, a, c, _] and the size is 4, you can return [d, d, d, d, c].

def replaceRemove(a, size):
    
    aEnhanced = []
    for i, j in enumerate(a):
        if j == 'a':
            for k in range(2):
                aEnhanced.append('d')
        elif j == 'b':
            pass
        else:
            aEnhanced.append(j)
    return aEnhanced[:size]

arr = ['a', 'b', 'c', 'a', 'd']
replaceRemove(arr, 4) # -> ['d', 'd', 'c', 'd']


# 6.5 - Test Palindromicity

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


# 6.6 - Reverse All The Words In A Sentence

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


# 6.7 - Compute All Mnemonics For A Phone Number

# Write a program which takes as input a phone number, specified as a string of digits, and returns all possible character 
# sequences that correspond to the phone number. The cell phone keypad is specified by a mapping that takes a digit and returns the 
# corresponding set of characters. The character sequences do not have to be legal words or phrases.

pad = {
    '0': '0',
    '1': '1',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrx',
    '8': 'tuv',
    '9': 'wxyz'
}



def WordsHelper(digits, word):
  
    letters = pad[digits[0]]    
#     print('letters -> {}'.format(letters))
    if len(digits) == 1:
        for letter in letters:
            print(word + letter) 
    else:
        for letter in letters:
            print('digits: {} wordletter: {}'.format(digits[1:], word+letter))
            WordsHelper(digits[1:], word+letter)         

def GenerateWords(digits):
    WordsHelper(digits, '')
    

GenerateWords('23')  


# 6.9 - Convert From Roman To Decimal

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


# 6.11 - Write A String Sinusoidally

# Write a program which takes as input a string s and returns the snakestring of s.

# For example, the snakestring for 'Hello World' is 'e lHloWrdlo!"
