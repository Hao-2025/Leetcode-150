# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement the encode and decode methods.

# How to solve this problem:
# 1. To encode a list of strings, we can use a delimiter to separate the strings.
# 2. To decode the string back to the original list, we can split the string using the same delimiter.



class Solution:

    def encode(self,strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self,s):
        res = []
        i = 0

        while i < len(str):
            j = i  # j = str.find('#',i)
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1 : j+1+length])
            i = j+1+length
        return res
    
    