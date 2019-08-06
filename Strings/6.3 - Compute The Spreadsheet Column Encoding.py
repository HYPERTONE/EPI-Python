
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
