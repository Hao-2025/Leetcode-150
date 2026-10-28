# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s1 cannot be a permutation inside s2
        if len(s1) > len(s2):
            return False
        
        # Initialize frequency arrays for 26 lowercase English letters (a-z)
        s1_count = [0] * 26
        window_count = [0] * 26

        # Populate frequency counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # If the first window matches s1's frequency, return True immediately
        if s1_count == window_count:
            return True
        
        # Slide the window across the rest of s2
        for r in range(len(s1), len(s2)):
            # Add the new character on the right side to the window
            window_count[ord(s2[r]) - ord('a')] += 1
            
            # Remove the old character on the far left side from the window
            left_char_idx = r - len(s1)
            window_count[ord(s2[left_char_idx]) - ord('a')] -= 1
            
            # Check if the updated window matches s1's frequency
            if s1_count == window_count:
                return True
                
        # Return False if no matching permutation window is found
        return False