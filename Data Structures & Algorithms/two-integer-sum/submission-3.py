'''
The reason that you didn't solve this faster was because you didn't understand how hashmaps worked 
in python
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        entries = {} 

        for i in range (len(nums)):

            compliment = target - nums[i]

            valid = entries.get(nums[i])
            if (valid!=None):
                print("hello")
                for key, value in entries.items():
                    print(key)
                    print(compliment)
                    if(key + compliment == target):

                        return [value, i] # return indices 
        
            entries[compliment] = i