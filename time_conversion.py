# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:56:50 2020

@author: Varad Srivastava

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in  hour format
Input Format

A single string  containing a time in -hour clock format (i.e.:  or ), where  and .

Constraints

All input times are valid
Output Format

Convert and print the given time in -hour format, where .

Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""

#!/bin/python3

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(":")
    meri = time[2][2:]
    time[2] = time[2][0:2]
    if meri=="AM":
        if time[0]!="12":
            return(":".join(time))
        else:
            time[0]="00"
            return(":".join(time))
    else:
        if time[0]!="12":
            time[0] = str(12+int(time[0]))
            return(":".join(time))
        else:
            #time[0]="12"
            return(":".join(time))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
