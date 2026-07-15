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

        Is because we've changed the condition of when the window moves. Amd this is the condition 

        nums[i] == nums[j] and abs( i - j) <= k
                              ^^^^^^^^^^^^^^^^^
                              this is a window right here. 
        
        Basically it is saying that in between these two ranges ( i - j) while being less than or equal to k. 

        Another reason to why you write your window like 

        R - L > K: # instead of 

        R - L + 1 > K:

        Also 
        '''
        for R in range(len(nums)):
            if abs(L - R) > k: 
                window.remove(nums[L])
                L+=1 
                print("Window has moved")
            if nums[R] in window:
                return True
            window.add(nums[R])
            print("Left value:", L)
            print("Right value:", R)
        
        return False 
