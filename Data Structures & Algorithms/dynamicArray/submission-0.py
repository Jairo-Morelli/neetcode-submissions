class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0 
        self.arr = [0] * capacity 

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n 
    '''
    Use the size of the array, which is the 
    amount of elements that exist in the array 
    as the index, then increment the size by one.

    Example:
     0  1  2  3  4  5 
    [1, 2, 3, 0, 0, 0]

    size = 3 

    arr[size]= 4 

    next Iter: 
    0  1  2   3  4  5 
    [1, 2, 3, 4, 0, 0]


    '''
    def pushback(self, n: int) -> None:
        # If the size is the same as the capacity 
        # resize the array
        if self.size == self.capacity: 
            self.resize()
        self.arr[self.size] = n 
        self.size +=1

    def popback(self) -> int:
        self.size -=1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        # Python you're intializing an array with this capacity.
        new_arr=[0] * self.capacity 

        # Copy old array into new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
