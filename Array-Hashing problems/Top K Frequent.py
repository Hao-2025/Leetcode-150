# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Ex:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


class Solution:
    def topKFrequent(self, nums: list[int], k:int):
        count = {} 
        for num in nums:
            count[num] = 1 + count.get(num,0)
        sorted_items = sorted(count.items(), key=lambda x:x[1],reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result