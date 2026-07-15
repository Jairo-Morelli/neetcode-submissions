class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        '''
        Example: 

        iter0:
            target = 12

            [0,2,4,6,8,10,12,14,16]
             l       m           r 
             0                   8 

        iter1: 
            target = 12 
            [8,10,12,14,16]
             l     m     r
             0  1  2  3  4 
        '''
        '''
        # Assuming that the numbers are ordered or sequntial 
        l, r = 0, len(nums) - 1


        while l <= r:
            
            m = (l + r) //2
           
           if nums[m] > target: 
            r = m - 1 
           if nums[m] < target:
            l = m + 1 
        

        return False 

        '''

        l,r = 0, len(nums)-1

        while l <= r: 

            m = (l + r) //2 

            if nums[m] > target:
                r = m - 1 
            if nums[m] < target:
                l = m + 1 

            if nums[m] == target: 
                return m 

        return -1 

        