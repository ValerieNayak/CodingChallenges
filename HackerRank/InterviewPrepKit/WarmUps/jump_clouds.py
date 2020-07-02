# Valerie Nayak
# @valyak on HackerRank
# January 3, 2020

def jumpingOnClouds(c):
    # c is an array of binary integers
    curr = 0    # current index
    end_index = len(c) - 1
    count_jumps = 0
    while curr < end_index:
        if curr+2 <= end_index and c[curr+2] == 0:
            curr += 2
        else:
            curr += 1
        count_jumps += 1
    return count_jumps

clouds = [0, 0, 0, 0, 1, 0]
print( jumpingOnClouds(clouds) )