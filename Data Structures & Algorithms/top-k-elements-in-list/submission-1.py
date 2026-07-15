class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        frequency = {} # O(n)
        mostK=[] #O(n)


        for i in range(len(nums)): 
            frequency[nums[i]]= frequency[nums[i]].get(nums[i], 0)+ 1 <- Remember this you're going to use it alot 
    
        for key, value in d.items():
            print(key, value)

            if value == k: 
                mostK.append(v)

        '''


        frequency = {}
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1 

        arr = list(frequency.items())

        # sort by value
        arr.sort(key=lambda x: x[1], reverse=True)

        mostFrequentK=[]
        for j in range(k):
            mostFrequentK.append(arr[j][0])
        
        return mostFrequentK