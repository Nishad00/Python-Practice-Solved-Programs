# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

# A valid mobile number is a ten digit number starting with a
# or

# .

# Concept

# A valid mobile number is a ten digit number starting with a
# or

# .

# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

# https://developers.google.com/edu/python/regular-expressions

# Input Format

# The first line contains an integer
# , the number of inputs.

# lines follow, each containing some string.

# Constraints

# Output Format

# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

# Sample Input

# 2
# 9587456281
# 1252478965

# Sample Output

# YES
# NO

import re
N = int(input())
for i in range(N):
    a = raw_input()
    l = len(a)
    matchObj = re.search("^[789][0-9]{9}$", a)
    if matchObj:
        print "YES"
    else:
        print "NO"
