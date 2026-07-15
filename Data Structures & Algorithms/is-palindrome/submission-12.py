class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r = 0, len(s) - 1 # Why? len gives you the size of the string, not the position of the final index

        # Basically alot of while loops 

        while l < r: 
            
            # Moving pointers
            while l < r and not self.checkIfAlpha_Numeric(ord(s[l])):
                l+=1 

            while r > l and not self.checkIfAlpha_Numeric(ord(s[r])):
                r-=1 

            if s[l].lower() != s[r].lower():
                return False
            l += 1 
            r -= 1 
            
        return True


    def checkIfAlpha_Numeric(self,code:int) -> bool: 
        if code > 47 and code < 57 or code > 64 and code < 91 or code > 96 and code < 123:
            return True
        else:
            return False