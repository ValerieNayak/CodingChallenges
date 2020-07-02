# Valerie Nayak
# 7/1/2020
# July LeetCode Challenge
# Day 1: Arranging Coins

def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    remaining = n
    k = 0 
    while remaining > 0:
        k += 1
        remaining -= k
    if remaining == 0:
        return k
    else:
        return k - 1

print(arrangeCoins(8))