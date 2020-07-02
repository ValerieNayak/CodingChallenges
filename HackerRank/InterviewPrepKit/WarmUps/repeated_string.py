# Valerie Nayak
# @valyak on HackerRank
# March 15, 2020

# Complete the repeatedString function below.
def repeatedString(s, n):
    # count the number of occurrences of 'a'
    total = 0     # this var will count all occurrences of a
    count_a = s.count('a')
    full_strings = n // len(s)
    total += count_a * full_strings
    r = n % len(s)  # remainder
    substring = s[:r]
    total += substring.count('a')
    return total

s = 'abcac'
n = 8
print(repeatedString(s, n))