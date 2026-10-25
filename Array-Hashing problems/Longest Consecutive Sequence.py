# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# EX:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


class Solution:
    def longestConsecutive(self, nums: list[int]):
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n-1) not in num_set:
                current_num = n
                current_length = 1
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)
       
        return longest