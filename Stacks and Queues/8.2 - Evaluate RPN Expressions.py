
# A string is said to be an arithmetical expression in Reverse Polish Notation (RPN) if:
# 1. It is a single digit or a sequence of digits, prefixed with an option - e.g. "6", "123", "-42"
# 2. It is of the form "A,B,o" where A and B are RPN expressions and o is the of the operators (+, -, x, /)

# For example, the following strings satisfy these rules: "1729", "3,4,+,2,x,1,+", "1,1,+,-2,x", "-641,6,.,28,/".

# An RPN expression can be evaluated uniquely to an integer, which is determined recursively. The base case corresponds to Rule (1), 
# which is an integer expressed in base-10 positional system. Rule (2) corresponds to the recursive case, and the RPNs are evaluated in
# the natural way, e.g., if A evaluates to 2 and B evaluates to 3, then "A,B,x" evaluates to 6.

# Write a program that takes an arithmetical expression in RPN and returns the number that the expression evaluates to.

def evaluate(RPN):
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
                '+' : lambda y, x: x + y,
                '-' : lambda y, x: x - y,
                '*' : lambda y, x: x * y,
                '/' : lambda y, x: int(x / y)
                }
    
    for token in RPN.split(DELIMITER):
        print('token: {}'.format(token))
        if token in OPERATORS:
            print(token)
            intermediate_results.append(OPERATORS[token](intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))
            print('inter-results: {}'.format(intermediate_results))
    return intermediate_results[-1]

myRPN = '3,4,+'
evaluate(myRPN) # -> 7
