# Give a string s, return true if it is a palindrome, or false otherwise.
# Consider only alphanumeric characters and ignore cases.
# Ex 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Ex 2:
# Input: "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right  and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -=1
            
        return True