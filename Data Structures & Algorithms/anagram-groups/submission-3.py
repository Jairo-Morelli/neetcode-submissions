class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ''' 

        Given an array of strings strs, group all anagrams together into sublist. You may return the output in any order. 

        An anagram is a string that contains the exact some characters as another string, but the order of the 
        characters can be different. 

        '''
        '''
        build array?

        The reason you're not able to "see" the solution to the problem, is simply you don't 
        understand all the "components" to the algortihm that you're writing.

        '''
        # time complexity: O(n * m)
        # space complexity
        chars = {} # Get creative with the keys and values key is total character value and value is going to be the string
        separated=None # he put an array inside of this somehow
        for i in range(len(strs)):
            stringval = 0 
            characters=[0] * 26
            for char in strs[i]:
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

                

            



