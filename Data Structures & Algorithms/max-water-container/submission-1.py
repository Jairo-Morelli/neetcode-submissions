class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        '''
        Two pointer solution: 

         [1,7,2,5,4,7,3,6]
            ^           ^ 
            l           r 
            1           6
    
  

        l = 0 
        r = len(heights)
        maxArea= 0 

        while(l<r):

            minHeight = min(heights[l],heights[r])

            currentArea = minHeight * (r-l) # l * w 

            if(currentArea>maxArea):
                maxArea=currentArea
      
            if heights[l] < heights[r]: 
                l +=1 
            else: 
                r -=1 

        return maxArea
        '''

        l = 0 
        r= len(heights) -1
        maxArea= 0

        while l<r:

            minHeight = min(heights[l], heights[r])
            
            currentArea = minHeight * (r-l) 

            if currentArea>maxArea:
                maxArea=currentArea
            
            if heights[l] < heights[r]:
                l+=1 
            else:
                r-=1
        
        return maxArea

