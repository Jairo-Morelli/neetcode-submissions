'''
    Don't forget about python's heap class
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largestK = k
        self.heap = nums
        heapq.heapify(self.heap)
                

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        print(self.heap)
        while len(self.heap) > self.largestK:
                heapq.heappop(self.heap)

        return self.heap[0]

       
        
