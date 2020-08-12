# Valerie Nayak
# LeetCode 8/12/2020
# 73 - set zeroes

def setZeroes(matrix):
    for rind, row in enumerate(matrix):
        for cind, pos in enumerate(row):
            if pos == 0:
                for temp_cind, item in enumerate(row):
                    if item != 0:
                        matrix[rind][temp_cind] = True
                for temp_rind, temp_row in enumerate(matrix):
                    if temp_row[cind] != 0:
                        matrix[temp_rind][cind] = True
    
    for rind, row in enumerate(matrix):
        for cind, pos in enumerate(row):
            if type(pos) == bool:
                matrix[rind][cind] = 0
    
    return matrix

# matrix = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
print(setZeroes(matrix))