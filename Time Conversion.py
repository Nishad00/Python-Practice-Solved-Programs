#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    received_date = s.split(':')

    time = received_date[2]

    if(time[2:] == "PM"):
        if(received_date[0] == "12"):
            received_date[0] = str(int(received_date[0]))
        else:
            received_date[0] = str(int(received_date[0]) + 12)
            
    if(time[2:] == "AM" and received_date[0] == "12"):
        received_date[0] = "00"


    new_date = ':'.join(received_date)

    return new_date[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()







# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# s: a string representing time in  hour format
# Input Format

# A single string  containing a time in -hour clock format (i.e.:  or ), where  and .

# Constraints

# All input times are valid
# Output Format

# Convert and print the given time in -hour format, where .

# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45