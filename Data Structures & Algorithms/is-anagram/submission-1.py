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
    
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        print(countS)
        print(countT)
        if countS == countT:
            return True
        else:
            return False
        


