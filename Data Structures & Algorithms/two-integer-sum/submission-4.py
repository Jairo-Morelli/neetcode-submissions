'''
The reason that you didn't solve this faster was because you didn't understand how hashmaps worked 
in python. 

The logic was soild, in terms of how to solve the answer. 

But surrounding how to use the hashmap you failed.

Also you don't really understand why, this is  O(n) time complexity and O(n) space complexity.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        entries = {} 

        for i in range (len(nums)):

            compliment = target - nums[i]

            if compliment in entries:
                return [entries[compliment],i]
        
            entries[nums[i]] = i