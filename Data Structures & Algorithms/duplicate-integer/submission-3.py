class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # if you're having identation problems, look at the outer 
        # statements and see if they are indented similarly.
        # time complexity: O(n)
        # space complexity: O(n)
        # space complexity because you added a dictionary, each time you check to see if a element 
        # is inside the dictionary you add it to the dictionary itself.
        duplicates = {}
        for i in nums:  
            if i in duplicates: 
                return True 
            else:
                duplicates[i]= False 

        return False
    