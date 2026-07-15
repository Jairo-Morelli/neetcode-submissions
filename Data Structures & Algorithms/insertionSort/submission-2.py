# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# The difference between this algorithm and mine: 
# One function exist to clone the pairs 
# One function to copy the states 
# You don't handle the pairs, straight off you actually copy them 
#  
# You (append)copy state at the beginning of the insertion sort 
# You (append)copy state during the middle of the insertion sort 
# You (append)copy state at the end of the insertion sort 
# 
#   The problem is the multiple different appending, if you're appending 
#   so much it probably means you don't know how your loop is working.
#
#
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i -1 
            
            while j >= 0 and  pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]

                j -=1
            res.append(pairs[:])
        return res