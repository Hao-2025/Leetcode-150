# Give two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# EX: "anagram" and "nagaram" are anagrams of each other.

class Solution:
    def isAnagram(self, s, t) -> bool:
        # 1. Check the length of two strings:
        if len(s) != len(t):
            return False
        
        # 2. Create 2 dict to store 
        countS, countT = {}, {}
        
        # 3. Count characters in string 
 
        for char in range(len(s)):
            countS[char] = countS.get(char, 0) + 1
            #countS[s[char]]= countS[s[char]] + 1
            #countS[s[char]]= countS.get[s[char],0] + 1 
    
            countT[char] = countT.get(char, 0) + 1
            
        # 4. Compare 2 dict countS and countT
        if countS == countT:
            return True
        else:
            return False