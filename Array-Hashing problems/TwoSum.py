
#Give a list integer number called "nums" and an integer number called  "target".
#Requirement: Sum of two numbers equal "target" number
#Then give indexes of these two numbers
#EX:
# Input
# nums = [2,7,11,15] target = 9
# Output
# [0,1] 

#Two sum
# How to solve (Using Hash Map_ Dictionary in Python)
# 1. Iterate through each element "num" at index "i" in the array.

# 2. Calculate the missing number needed (called complement): complement = target - num

# 3. Check if complement exists in the Hash Map:
# If yes: This means we have found the pair; return the index of complement in the Map and the current index i.
# If not: Store num and its index i into the Hash Map, then continue iterating.


class Solution:
   def twoSum(self, nums, target):
      prevMap = {} # value : index 
    
      for i, n in enumerate(nums):
         complement = target - n
         if complement in prevMap:
            return [prevMap[complement], i]
         prevMap[n] = i
      return []


