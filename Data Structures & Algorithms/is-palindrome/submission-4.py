'''
This solution is 
    - Two pointer 
    - unicode ascii help 
    - a while loop 
    - order execution
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start, end = 0, len(s)-1

        while start < end:
            
            charStart = s[start]
            charEnd = s[end]

            if start==end:
                break

            if self.checkIfAlpha_Numeric(ord(charStart.lower())):
            
                print("Left pointer",charStart.lower(), start)
                while True: 
                        #if the right side isn't alphanumeric, you can skip it here. You only compare if alphaNumeric
                    if self.checkIfAlpha_Numeric(ord(charEnd.lower())):
                        if charStart.lower() != charEnd.lower():
                            return False
                        else:
                            start+=1 
                    else:
                        print("right pointer wasn't alpha numeric")
                    break     
            else:
                start+=1 
                print("move left pointer")

            if self.checkIfAlpha_Numeric(ord(charEnd.lower())):
                print("right pointer",charEnd.lower(),end)
                while True:
                    # if the right side isn't alphanumeric, you can skip it here. You only compare if alphaNumeric
                    if self.checkIfAlpha_Numeric(ord(charStart.lower())):
                        if charStart.lower() != charEnd.lower():
                            return False
                        else:
                            end-=1
                    else:
                        print("left pointer wasn't alpha numeric")
                    break
            else: 
                end-=1 
                print("move right pointer")

            
        return True

    def checkIfAlpha_Numeric(self,code:int) -> bool: 
        if code > 47 and code < 57 or code > 64 and code < 91 or code > 96 and code < 123:
            return True
        else:
            return False    