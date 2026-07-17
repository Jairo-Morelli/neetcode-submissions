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

        for i in nums: 
            entries[i] = entries.get(i,0) + 1

        sorted_by_keys = list(sorted(entries.items(), reverse=True, key= lambda item: item[1])) 

        most_k = []

        for j in range(k):
            most_k.append(sorted_by_keys[j][0])

        return most_k