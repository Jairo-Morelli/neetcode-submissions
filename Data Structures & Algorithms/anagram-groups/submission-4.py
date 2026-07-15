class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ''' 

        Given an array of strings strs, group all anagrams together into sublist. You may return the output in any order. 

        An anagram is a string that contains the exact some characters as another string, but the order of the 
        characters can be different. 

        '''
        '''
        The key strategy here, is basically you have to map, the characters in a way, 
        that you can store them properly as a key. 

        so that you can then access them via that key
        '''
        # time complexity: O(n * m)
        # space complexity: O(n * m )
        chars = {} # O(n) space Get creative with the keys and values key is total character value and value is going to be the string
        separated=None # O(m) he put an array inside of this somehow
        for i in range(len(strs)): # O(n) time
            stringval = 0 
            characters=[0] * 26
            for char in strs[i]: # O(m) time, each character
                stringval= ord(char)
                characters[stringval-ord("a")] +=1
            # the key would be a word, but you would convert to see if they same the same 
            # characters, through the way that you map them 


            if tuple(characters) in chars:
                chars[tuple(characters)].append(strs[i])
                print("key found")
            else:
                chars[tuple(characters)] = chars.get(tuple(characters),[strs[i]])


            
        separated= list(chars.values())
        print(separated)

           
        return separated

                

            



