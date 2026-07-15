class MinHeap:
    
    def __init__(self):
        self.heap = [0] # Dummy value
        

    def push(self, val: int) -> None:
        self.heap.append(val) # There is no guarantee that this will preserve the sorted property
        self._bubble_up(len(self.heap)-1) # We have to pass the index of where we want to bubble up from as well. In this case it will be at the end of the list

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop() # pop the element in front and return the element at index 2, which will be a value.

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums  # concatiate position [0] of self.heap and nums
      
        for i in reversed(range(1, len(self.heap) // 2 + 1)): # This becomes O(n) because it is amorizated, you're only ever bubbling down half of the tree at a time.
            self._bubble_down(i)

    # Snake Case
    # For bubbling up a value to its parent.
    def _bubble_up(self, index):
        parent = index // 2 # left child 
        while index > 1 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index] # Switch values here
            index = parent  # Switch indices 
            parent = index // 2 # Switch indices
    
    # Snake Case
    def _bubble_down(self, index):
        child = 2 * index # left child 
        while child < len(self.heap):
            if child + 1 <  len(self.heap) and self.heap[child + 1 ] < self.heap[child]:
                # right child is smaller
                child +=1
            
            if self.heap[child] >= self.heap[index]:
                return

            self.heap[child],self.heap[index] = self.heap[index],self.heap[child]
            index = child
            child = 2 * index
        