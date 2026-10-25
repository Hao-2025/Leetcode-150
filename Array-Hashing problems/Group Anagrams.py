#Give an array of strings called "strs" and group the anagrams together. You can return the answer in any order.
#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Example:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# How to solve (Using Hash Map_ Dictionary in Python)

# 1. Create a dictionary to hold the grouped anagrams.
# 2. Iterate through each string in the input list.
# 3. Sort the characters of the string to create a key for the dictionary.
# 4. If the key is not in the dictionary, create a new entry with the key and an empty list.
# 5. Append the original string to the list corresponding to the key in the dictionary.
# 6. Finally, return the values of the dictionary as a list of lists.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        grouped = defaultdict(list) # Dict to hold grouped anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            grouped[tuple(count)].append(s)

        return list(grouped.values())   