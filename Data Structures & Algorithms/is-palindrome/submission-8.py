class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The only thing, that I think that won't work 
        # in this case is that my string has spaces in it
        s = s.lower()
        s = s.replace(" ", "")

        for i in s: 
            if not self.checkIfAlpha_Numeric(ord(i)):
                s=s.replace(chr(ord(i)),"")

        
        print(s)
        l, r = 0, len(s)-1      
        while l < r: 
            # edge case
            if l == r:
                break 
           

            if s[l]==s[r]:
                print("left pointer: "+ s[l])
                print("right pointer: "+ s[r])
                l+=1 
                r-=1 
            else:
                return False
            
        
        return True


    def checkIfAlpha_Numeric(self,code:int) -> bool: 
        if code > 47 and code < 57 or code > 64 and code < 91 or code > 96 and code < 123:
            return True
        else:
            return False