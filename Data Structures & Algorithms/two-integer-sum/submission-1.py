# Time complexity O(n)
# Space complexity O(n) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        entries = {}
        pair = []
        '''
        Key is complement, value is the index the complement is stored.
        '''

        for i in range(0, len(nums)): 
            compliment = target - nums[i]
            
            if nums[i] in entries:
                pair = [entries[nums[i]], i]
            else: 
                entries[compliment] = i 

        print(entries)
        return pair

