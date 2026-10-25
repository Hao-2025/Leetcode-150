#Give a list integer number called "nums". Return True if any value appears at least twice in the array, and return False if every element is distinct.

#EX: [1,2,3,1] => True
#    [1,2,3,4] => False
#    [1,1,1,1] => True

# Contains Duplicate
# How to solve (Using Set in Python)

# 1. Create an empty set to store seen numbers.
# 2. Iterate through each number in the array.
# 3. If the number is already in the set, return True (duplicate found).
# 4. If not, add the number to the set.
# 5. If the loop completes without finding duplicates, return False.


class Solution:
   def containsDuplicate(self,nums):
      hashSet = set()  # Create an empty set to store seen numbers.
      for num in nums:
         if num in hashSet:
            return True #(duplicate found)
         hashSet.add(num) # Add number to the set if not already present.
      return False #(no duplicates found)