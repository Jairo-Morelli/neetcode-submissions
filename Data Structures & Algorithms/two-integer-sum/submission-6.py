class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        target = 7
        [3, 4, 5, 6]
         0 
         i 

         sum =  7 - 3 

         4 

         if 4 is in compliment_hash  
            return the value of that compliment 
            which is 3, in this case


        compliment = {}

        for i in range(len(nums)):

          sum = target - nums[i] 

          if sum in compliment: 
            return [compliment[sum],i]
        
          compliment[sum] = i 

        return [] 
        '''

        compliment = {}

        for i in range(len(nums)): 

            sum = target - nums[i] # here you are finding the compliment of the current index value, so for 3 it will be 4. 

            if nums[i] in compliment: # but here you are looking if the current index value has already an compliment, so for the first iteration if 3 has a compliment
                return [compliment[nums[i]], i]

            compliment[sum] = i 
        
        return []
     