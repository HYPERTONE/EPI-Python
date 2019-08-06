
# Write a program which takes as input a phone number, specified as a string of digits, and returns all possible character 
# sequences that correspond to the phone number. The cell phone keypad is specified by a mapping that takes a digit and returns the 
# corresponding set of characters. The character sequences do not have to be legal words or phrases.

def mneumonic(digits, word):
    
    letters = pad[digits[0]]
    
    if len(digits) == 1:
        for letter in letters:
            print(letter + word)
    else:
        for letter in letters:
            mneumonic(digits[1:], word + letter)
    
    

mneumonic('32', '')
