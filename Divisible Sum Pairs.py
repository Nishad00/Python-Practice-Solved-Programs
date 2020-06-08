#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    list1 = [i for i in range(n)]
    list1 = list(combinations(list1,2))
    for i,j in list1:
        if i < j and (ar[i]+ar[j])%k == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


















# You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .

# For example,  and . Our three pairs meeting the criteria are  and .

# Function Description

# Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

# divisibleSumPairs has the following parameter(s):

# n: the integer length of array 
# ar: an array of integers
# k: the integer to divide the pair sum by
# Input Format

# The first line contains  space-separated integers,  and .
# The second line contains  space-separated integers describing the values of .

# Constraints

# Output Format

# Print the number of  pairs where  and  +  is evenly divisible by .

# Sample Input

# 6 3
# 1 3 2 6 1 2
# Sample Output

#  5
# Explanation

# Here are the  valid pairs when :

