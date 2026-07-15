class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 

        brute force:
        max_water=0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):    
                min = min(heights[i], heights[j])   

                current_area= min * (j - i) # l * w 

                if(max_water<current_area):
                    max_water = current_area

                
        return max_water


        Time complexity: O(n^2)
        Space complexity: O(1)
        
        '''

        max_water = 0 
        
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):

                minimum = min(heights[i], heights[j])

                current_area = minimum * (j - i) 

                print("minimum height value:",minimum)
                print("current_area value:",current_area)

                if (max_water< current_area):
                    max_water = current_area

        return max_water 