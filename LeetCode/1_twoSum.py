# Valerie Nayak
# 7/1/2020
# LeetCode: Two Sum

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind1, num1 in enumerate(nums):
            for ind2, num2 in enumerate(nums[ind1+1:]):
                if num1 + num2 == target:
                    return [ind1, ind1 + 1 + ind2]
        return None