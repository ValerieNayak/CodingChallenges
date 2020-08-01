# Valerie Nayak
# 8/1/2020
# LeetCode Mock Interview: Q11
# Container With Most WAter

def maxArea(height):
    p1 = 0
    p2 = len(height) - 1
    maxArea = 0
    while p1 < p2:
        area = min(height[p1], height[p2]) * (p2 - p1)
        if area > maxArea:
            maxArea = area
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return maxArea