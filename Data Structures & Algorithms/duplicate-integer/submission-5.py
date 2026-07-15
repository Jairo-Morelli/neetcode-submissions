# Do Brute Force than do optimize 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        [1, 2, 3, 3]
               i  j          
        for i in nums:
            for j in nums(advanced + 1): 

                if i == j: 
                    return True 
            
        return False 
        '''
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # On
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates: 
                return True 
            duplicates[nums[i]]=1 
        return False 