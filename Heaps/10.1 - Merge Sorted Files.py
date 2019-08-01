
# 10.1 - Merge Sorted Files

# You are given 500 files, each containing stock trade information for an S&P 500 company. Each trade is encoded by a line in 
# the following format: 1232111,AAPL,30,456.12.

# The first number is the time of the trade expressed as the number of milliseconds since the start of the day's trading.
# Lines within each file are sorted in increasing order of time. The remaining values are the stock symbol,
# number of shares, and price.

# You are to create a single file containing all the trades from the 500 files, sorted in order of increasing trade times.
# The individual files are of the order of 5 - 100 megabytes; the combined file will be of the order of 5 gigabytes. In the
# abstract, we are trying to solve the following problem.

# Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.
# For example, if the input is <3, 5, 7>, <0, 6>, and <0, 6, 28>, then the output is <0, 0, 3, 5, 6, 6, 7, 28>.


# This is actually pretty cool

def mergeSortedArrays(arrays):
    return list(heapq.merge(*arrays))
    
mergeSortedArrays([[3, 5, 7], [0, 6], [0, 6, 28]]) # -> [0, 0, 3, 5, 6, 6, 7, 28]

# Note that * unpacks the list of lists. So [[3, 5, 7], [0, 6], [0, 6, 28]] becomes [3, 5, 7] [0, 6] [0, 6, 28]
# which is a valid input in merge such as list(heapq.merge([9,2], [3,4])) will return [3, 4, 9, 2]
