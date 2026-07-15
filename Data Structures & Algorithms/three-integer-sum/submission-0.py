class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        '''
        triples =[]

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                for k in range(j+1,len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0: 

                        triples.append([nums[i],nums[j],nums[k]])

        return triples
                    
        time complexity: O(n^3)
        space complexity:O(n)
        '''

        triples = set()

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                for k in range(j+1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:
                        tempTriple = sorted([nums[i],nums[j],nums[k]])

                        tempTriple = tuple(tempTriple)

                        triples.add(tempTriple)

        return [list(i)for i in triples] # quick way of iterating through 