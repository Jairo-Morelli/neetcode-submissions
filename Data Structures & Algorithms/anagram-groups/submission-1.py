class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' 
        You don't need that many for loops 
        what I think the brute force solution looks like 

        1. break up apart the current string index
        2. Match it with a string with the same character frequency
        3. Once you find the match add both strings inside an list

        two hash maps 
            - One that breaks down the characters and compares the matching string 
            - One that stores the word and its index inside the original string array.
        '''
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs: 
            count = [0] * 26 # a ... z this is for each individual string, you're creating an count for all potential characters from a ... z

            for c in s: 
                count[ord(c) - ord("a")] += 1 # you're mapping because you need a value that represents "A"

            res[tuple(count)].append(s)

        print(list(res.values()))
        return list(res.values())
        
            