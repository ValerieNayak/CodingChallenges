# Valerie Nayak
# @valyak on HackerRank
# January 3, 2020

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # s is a string of length n
    prev = 0
    curr = 0
    valley_count = 0
    for char in s:
        prev = curr
        if char == 'U':
            curr += 1
        else:
            curr -= 1
        if prev<0 and curr==0:
            valley_count += 1
    return valley_count

path = 'UDDDUDUU'
print(countingValleys(len(path), path))
