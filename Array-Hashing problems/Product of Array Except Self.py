# Given an integer array nums, return an array answer such that answer [i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix of suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that run in O(n) time with out using the division operation.

#Ex:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Input:  [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# How to solve
# 1. Create an output array and initialize it with 1s.

# 2. Traverse the input array from left to right, and for each element, update the output array with the product of all previous elements.

# (EASILY FOR IMAGINE:from left to right: go through the array and "MULTIPLY" the current element with the "PREVIOUS" product and store it in the output array)

# 3. Traverse the input array from right to left, and for each element, update the output array with the product of all subsequent elements.

# (EASILY FOR IMAGINE: from right to left: go through the array and "MULTIPLY" the current element with the "NEXT" product and store it in the output array)

# 4. Return the output array.

class Solution:
    def productExceptSelf(self,nums):
        
        res = [1] * len(nums)
        prefix_product = 1
        for i in range(len(nums)):
            res[i] = prefix_product
            prefix_product *= nums[i]

        right_product = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res