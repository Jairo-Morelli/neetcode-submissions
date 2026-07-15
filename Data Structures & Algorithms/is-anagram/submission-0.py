# Time Complexity O(n + m) 
# n = s (len of s)
# m = t (len of m)
# Space Complexity is O(1)
# because no additional data structures are being used
# and copying the strings. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        return sorted(s) == sorted(t)


