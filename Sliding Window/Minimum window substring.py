# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, return an empty string
        if t == "": return ""

        # countT stores the required frequency of each character in t
        # window stores the frequency of characters in the current sliding window
        countT, window = {}, {}

        # Populate the frequency map for string t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'have' tracks how many unique characters currently meet the required frequency
        # 'need' is the total number of unique characters required from t
        have, need = 0, len(countT)
        
        # Track the start/end indices and the minimum length of the valid window found
        res, resLen = [-1, -1], float("infinity")
        
        # Left pointer of the sliding window
        l = 0
        
        # Expand the window by moving the right pointer (r) across string s
        for r in range(len(s)):
            c = s[r] 
            window[c] = window.get(c, 0) + 1  # Add the right character to the window

            # If the current character's count matches its required count in t, increment 'have'
            if c in countT and window[c] == countT[c]:
                have += 1

            # When the window satisfies all requirements (have == need), try to shrink it
            while have == need:
                # Update our result if the current window is smaller than the previous minimum
                if (r - l + 1) < resLen: 
                    res = [l, r]         
                    resLen = (r - l + 1)

                # Pop/remove the character at the left pointer from the window
                window[s[l]] -= 1  
                
                # If removing the left character causes it to drop below the required count, decrement 'have'
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                # Shrink the window from the left side
                l += 1
                
        # The best indices found
        l, r = res
        
        # Return the minimum window substring, or an empty string if no valid window was found
        return s[l:r + 1] if resLen != float("Infinity") else ""