# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        print("size of array: ", len(pairs))
        return self.mergeSortHelper(pairs,0, len(pairs) - 1)
        
      

    def mergeSortHelper(self, pairs: List[Pair], start :int, end:int) -> List[Pair]:
        

        # the reason that this isn't working is that the 
        # merge function is returning a arr[k] = (out of bounds)
        print("start value(0):", start)
        print("end value(0): ", end)
        # Base case 
        if end - start + 1 <= 1: 
            return pairs 
        
        # Recursive case 
        m =  (start + end) // 2 
        self.mergeSortHelper(pairs, start, m) # Basically the error here, is that the base case doesn't get reached. The reason this isn't working
        print("start value(1):", start)
        print("end of array value(1): ", end)
        self.mergeSortHelper(pairs, m+1, end) # is because this isn't working
        print("start value(2):", start)
        print("end of array value(2): ", end) # when end reaches 5, you have a problem.


        self.merge(pairs,start,m,end) 

        return pairs


    # merge in place
    def merge(self, arr, s, m, e):
        # copy the sorted left & right halfs to temp arrays 
        L = arr[s:m + 1] # The start is inclusive, the end is exclusive
        R = arr[m + 1: e + 1] # The start is inclusive, the end is exclusive
 
        i = 0 # index for L
        j = 0 # index for R 
        k = s # index for arr

        # Merge the two sorted halfs into the original array 
        # sort the halves 
        while i < len(L) and j < len(R):

            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i +=1
                k +=1 
            else: 
                arr[k] = R[j]
                j += 1 
                k += 1

        # One of the halves will have elements remaining 
        # you're just copying over, here you're not actually re-sorting
        # this is like a check 
        # exhaust left array
        while i < len(L): 
            arr[k] = L[i]
            i += 1 
            k += 1 
        # exhaust right array
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1 

        for p in arr:
            print("key:", p.key)


        return arr
