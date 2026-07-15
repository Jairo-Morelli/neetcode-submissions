class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        You are given an integer array nums and an integer k, return true if there are two distinct indices. 
                                                                                       ^^^^^^^^^^^^^^^^^^^^^


        i and j in the array such that nums[i] == nums[j] and abs(i - j) <=k, other wise return false. 



        nums = [1, 2, 3, 1] 
        k= 1

        nums[0] == nums[3] and abs( 0 - 3) <- in this specific case it turns to 1, not 3 <= 3 (false)



        nums = [2, 1, 2]
        k = 1 

        nums[0] == nums[1] and abs(0 - 2) <= 1 (false)

        if 3 - 1 > 2: 


        1st 
            for r in range (len(nums)):
                if 0 - 1 > 2 

        2nd 
            for r in range (len(nums)):
                if 1 - 1 > 2 
        
        3rd for r in range (len(nums)):
                if 2 - 1 > 2 
        
        '''
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                    window.remove(nums[l])
                    l += 1 
            if nums[r] in window:
                    return True 
            window.add(nums[r])
        return False 