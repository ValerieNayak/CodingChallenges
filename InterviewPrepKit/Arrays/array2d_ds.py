# Valerie Nayak
# @valyak on HackerRank
# 3/17/2020

def hourglassSum(arr):
    max = None     # var to store max hourglass sum
    for r in range(1, len(arr)-1):
        for c in range(1, len(arr[r])-1):
            sum = 0
            coords = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c), (r+1, c-1), (r+1, c), (r+1, c+1)]
            for point in coords:    # each point is a tuple
                sum += arr[point[0]][point[1]]
            if max == None or sum > max:
                max = sum
    return max

# arr = [[1, 1, 1, 0, 0, 0,],
# [0, 1, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0],
# [0, 0, 2, 4, 4, 0],
# [0, 0, 0, 2, 0, 0],
# [0, 0, 1, 2, 4, 0]]

arr = [[-1, 1, -1, 0, 0, 0],
[0, -1, 0, 0, 0, 0],
[-1, -1, -1, 0, 0, 0],
[0, -9, 2, -4, -4, 0],
[-7, 0, 0, -2, 0, 0],
[0, 0, -1, -2, -4, 0]]

print(hourglassSum(arr))
