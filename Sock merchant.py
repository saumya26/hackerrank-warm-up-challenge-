#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_count = 0
    for i in Counter(ar).values():
        pair_count+= i//2
    return pair_count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
