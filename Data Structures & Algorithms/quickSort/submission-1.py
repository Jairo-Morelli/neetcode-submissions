# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
     return self.quickSortHelper(pairs,0,len(pairs)-1)

    def quickSortHelper(self, pairs:List[Pair], s: int, e: int ) -> list[Pair]: 
        
        if e - s + 1 <=1:
            return pairs 

        pivot = pairs[e] # we are using the final element as the pivot
        left = s # pointer for leftside 

        #Partition: Elements smaller than pivot left side 

        for i in range(s,e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left] # assign temporary to left pointer element
                pairs[left] = pairs[i] # reassign the element @ left pointer i.e not re-assigning the left pointer. 
                pairs[i] = tmp # assign left pointer element to element at index i. 
                left += 1 


        # Note pivot between left & right sides 
        pairs[e] = pairs[left]
        pairs[left] = pivot 

        # Quick sort left side 
        self.quickSortHelper(pairs,s,left-1)
        # Quick sort right side 
        self.quickSortHelper(pairs,left+1,e)

        return pairs 