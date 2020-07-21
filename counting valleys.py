Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=count=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                count+=1
        else:
            level-=1
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = str(input())

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
