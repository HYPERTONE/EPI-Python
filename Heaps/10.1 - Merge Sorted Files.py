
# A heap is a specialized binary tree. The keys must satisfy the heap property - the key at each node is at least as great
# as the keys stored at its children.

# A heap is sometimes referred to as a priority queue because it behaves like a queue, with one difference: each element has a 
# 'priority' associated with it, and deletion removes the element with the highest priority.

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
