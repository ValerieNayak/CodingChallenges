# Valerie Nayak
# @valyak on HackerRank
# January 2, 2020

#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # n is int length of input
    # ar is list of ints
    socks_dict = {}
    pair_count = 0
    for s in ar:
        if s in socks_dict:
            socks_dict[s] += 1
            if socks_dict[s] % 2 == 0:
                pair_count += 1
        else:
            socks_dict[s] = 1
    return pair_count

total_socks = 9
socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(total_socks, socks))