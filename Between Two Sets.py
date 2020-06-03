#!/bin/python3

import math
import os
import random
import re
import sys

def factor(i,a):
    
    for j in a:
        if i%j == 0:
            pass
        else:
            return False
    return True

def factor2(i,b):
    
    for j in b:
        if j%i == 0:
            pass
        else:
            return False
    return True
    


def getTotalX(a, b):

    a_list1 = []
    a_factor_list1 = []
    b_factor_list1 = []

    for i in range(a[0],b[0]+1):
        a_list1.append(i)
    
    for i in a_list1:
        if(factor(i,a)):
            a_factor_list1.append(i)

    for i in a_factor_list1:
        if(factor2(i,b)):
            b_factor_list1.append(i)
      
    
    
    return len(b_factor_list1)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()




















# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

# For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

# a: an array of integers
# b: an array of integers
# Input Format

# The first line contains two space-separated integers,  and , the number of elements in array  and the number of elements in array .
# The second line contains  distinct space-separated integers describing  where .
# The third line contains  distinct space-separated integers describing  where .

# Constraints

# Output Format

# Print the number of integers that are considered to be between  and .

# Sample Input

# 2 3
# 2 4
# 16 32 96
# Sample Output

# 3
# Explanation

# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.

# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.








