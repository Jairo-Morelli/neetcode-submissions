class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Completely over thinking, 
            why don't I just do this, since i have to c
            alculate an output where output[i] is all the product 
            of all the elements of nums except nums[i]. 
            if the list has a length of 4, 
            that means only 3 calculations are being done on all 4 indices. 
            if the list has a length of 6, that 
            means only 5 calcluations are being done on all 6 indices.
        '''
      

        n = len(nums)
        res = [0] * n
        final_product = 1
        zero_count = 0
        zero_index = 0

        for i in range(0, n):
            if nums[i] == 0: 
                zero_count+=1
                zero_index = i 
                
            if zero_count == 2:
                res = [0] * n
                return res
            if nums[i] == 0:
                continue
            final_product *= nums[i]

        for j in range(0, n):
            if zero_count == 1: 
                if nums[j] == 0:
                    continue
                res[zero_index] = final_product
              
            elif zero_count == 0:
                res[j] = final_product // nums[j]

        return res
    
