import heapq
class KthLargest:

    #Time complexity nlogn
    def __init__(self, k: int, nums: List[int]):
       self.largest_k = k 
       self.minHeap = nums 

       heapq.heapify(self.minHeap)
       while len(self.minHeap) > self.largest_k: 
            heapq.heappop(self.minHeap)

    #Time complexity: logn
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        # looks like you're going to have to heapfiy again somewhere here
        # the only time you want to pop from the min heap is when you have less elements 
        # than k

        if len(self.minHeap) > self.largest_k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        
