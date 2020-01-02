# Valerie Nayak
# @valyak on HackerRank
# January 2, 2020

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print('n', n)
    print('ar', ar)

    fptr.write(str(result) + '\n')

    fptr.close()
