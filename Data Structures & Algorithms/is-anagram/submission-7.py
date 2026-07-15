'''
If think in order to get really good at leetcode or DSA style problems, 
you simple just need to learn how to read DSA styled questions and 
then as well learn how to read your own code. 
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictionary = {} # Create dictionary 
        # Isn't a anagram
        if len(s) != len(t): # If both the length of s and t aren't equal 
            return False 

        for char in s:
            dictionary[char]= dictionary.get(char, 0) + 1  # key s equals .get(s(key), 0(default value)), plus one
            #print(char)



        print(dictionary)        
        for char in t: # for single character in t 
            print(char)
            if char in dictionary:  # if a single character is in dictionary check 
                if dictionary[char] !=0: # if the value of key of a single charater 
                    dictionary[char] -=1 
                else:
                    return False
            else:
                return False

        return True 

