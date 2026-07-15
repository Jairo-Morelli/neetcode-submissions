class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''

        entries = {}

        # you are going to get the frequencies of each number in nums
        for i in nums: 
            entries = entries.get(nums[i],0) + 1 

        sorted_by_keys = dict(sorted(data.items()))
        most_k = []

        for j in range(k):
            most_k.append(sorted_by_keys[j])

        return most_k            
        ''' 


        entries = {}

        for i in range(len(nums)): 
            entries[nums[i]] = entries.get(nums[i], 0) + 1 

        couple = list(sorted(entries.items(), reverse=True, key=lambda item: item[1]))

        most_k = []

        for i in range(k):
            most_k.append(couple[i][0])
            

        return most_k