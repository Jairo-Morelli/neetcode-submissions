class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Given an integr array nums and an integer k, return the k most frequent elements within the 
            array. The test cases are generated such that the answer is always unique. 
        '''
        
        '''
             I know you can use a priority queue. Here, so what I am actually going to do right now, is follow through watching 
             a video about a priority queue.
        '''

        '''
           [1, 2, 2, 3, 3, 3]  k= 2
            0  1  2  3  4  5
               i

            frequencies= { 1:1 }

        2nd iter 

            frequencies = { 1:1 , 2: 1 } 
        
        3rd iter 

            frequencies = { 1:1 , 2: 2}
        
        4th iter 

           frequencies = { 1:1, 2:2, 3:1}
        
        6th iter and final iteration 

          frequencies =  { 1:1, 2:2, 3:3}

        
        If you do it this way, you have to check for the values of you keys in your hash map 

        for key, value in frequencies.items(): 
            if value >= k:
             container.append(key)   

        return container
        
        '''

        frequencies = {}
        container = []

        for i in range(len(nums)): 
            frequencies[nums[i]]= frequencies.get(nums[i], 0) + 1

        for key, value in frequencies.items():
                container.append((key,value))

        container.sort(key=lambda x: x[1], reverse=True)

        result = []

        for j in range(k):
            result.append(container[j][0])
        

        return result