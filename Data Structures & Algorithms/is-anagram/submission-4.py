class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        input: s = "racecar" , t = "carrace" 

        Output: true 

        An anagram is a string that contains the eaxt same characters as another string, but the 
        order of the characters can be different. 

        characters the same but, different word. 

        1. two for loops, whatever element you're currently at, look for the other in a for loop, in the other
        2. You just gather the frequency of the characters(optimized)
        '''

        #Because they are an anagram, first check to see if they have the same amount of characters 

        frequency = {}
        frequencytwo = {}
        if not len(s) == len(t):
            return False 

        for i in range(len(s)):
            frequency[s[i]] = frequency.get(s[i], 0) + 1
        
        for i in range(len(t)):
            frequencytwo[t[i]] = frequencytwo.get(t[i], 0) + 1 
        

        if frequency == frequencytwo:
            return True
        return False
                