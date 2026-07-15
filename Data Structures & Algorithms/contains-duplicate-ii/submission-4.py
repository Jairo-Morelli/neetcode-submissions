class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set() 
        L = 0 

        # R is i in this case 
        # L is j in this case
        ''' 
        The reason that this DSA problem uses 
        
        R - L > k instead of 

        R - L + 1 > k 

        Is because we've changed the condition of why the window moves.
        '''
        for R in range(len(nums)):
            if R - L > k: 
                window.remove(nums[L])
                L+=1 
                print("Window has moved")
            if nums[R] in window:
                return True
            window.add(nums[R])
            print("Left value:", L)
            print("Right value:", R)
        
        return False 
