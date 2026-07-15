class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        '''
            How to remove a character if it isn't alpha numeric, or ignore if it isn't alphanumeric.

            If there is a space in the string, you can skip because of alphanumeric. 

            You actually gain some advantages by comparing the char's within a string.

            for char in range(len(s)):
                if s[char].isalnum(): 

                    if newStr[char].isalnum(
        '''

        for char in range(len(s)):
            if s[char].isalnum(): # why am I only checking if one word is a plaindrome? It is the same string that I am checking not another
                newStr += s[char].lower()
            else:
                pass

        
        return newStr==newStr[::-1]        
            