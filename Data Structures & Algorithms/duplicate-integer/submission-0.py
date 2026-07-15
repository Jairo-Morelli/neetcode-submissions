class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {} # dictonary 

        for i in range(0,len(nums)):
            value = nums[i]

            '''
            Okay the reason this works is: 
            you're going to check if the value 
            is in the hashmap. 

            if the condition is true, 
            return true. 

            if the condition is false, which means 
            that the the value doesn't exist within the hashmap
            assign the value within the hashmap and assign it to False.  
            '''
            if value in hashmap:
                hashmap[value] = True # I am just doing this to be extra
                return True
            else:
                hashmap[value] = False
        return False