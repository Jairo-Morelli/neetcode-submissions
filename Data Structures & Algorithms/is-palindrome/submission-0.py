import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:

    
        '''
        Can I get an explaination here? 

        A palindrome has this characteristic, that if you reverse at any end of the sentence, 
        it will spell the same word. 

        r a c e c a r -> r a c e c a r 
        0 1 2 3 4 5 6    6 5 4 3 2 1 0 

        If the word itself is spelt the same, reversed, that means that each character. 

        Here is the correlation, so @ 0 there is the same character @len(str) if plaindrome. 

        @ 1 there is the same character @len(str)-1 if plaindrome. 

        @ m, n being the middle of the of the string @len(str)/2, in all cases should return the same character. This 
        condtion should be true, even if it is not a plaindrome. 

        How am I suppose to make this case-insensitive and irgnore all non-alphanumeric characters?

        regular expression is a very powerful tool for string manipulation.
        '''
        clean_text= re.sub(r'[^\w\s]', '', s)
        clean_text= re.sub('\s','',clean_text)
        print(clean_text)
        lower = clean_text.lower() 
        print(lower)
        start=0 
        end = len(lower)-1 # I want the actual end position, not the size of the s.
        while start<end: # start < end because you need to check for start==end case. 
            start_s=lower[start] 
            end_s= lower[end]
            print(end_s)

            if start_s !=end_s:
                return False

            start+=1 
            end-=1 
        
        return True


