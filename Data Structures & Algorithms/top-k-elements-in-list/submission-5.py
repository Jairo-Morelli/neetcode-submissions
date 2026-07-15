import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequent_k = []
        dictionary = {}



        for i in nums:
            dictionary[i] = dictionary.get(i, 0) + 1 
            
        for key, v in dictionary.items(): 
            frequent_k.append((key,v))

        sorted_frequent_k = sorted(frequent_k, key=lambda item: item[1],reverse=True)
        print(sorted_frequent_k)
        final_res = []
        for j in range(k):
            print(j)
            final_res.append(sorted_frequent_k[j][0])

        return final_res

        