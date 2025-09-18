# Last updated: 19/09/2025, 00:17:25
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq=defaultdict(int)

        # for num in nums:
        #     freq[num]+=1
        # print(freq)
        
        # sorted_nums=sorted(freq,key=freq.get,reverse=True)
        # print(sorted_nums)
        # return sorted_nums[:k] 

        freq_map=Counter(nums)
        result=[]

        bucket= [[] for _ in range(len(nums)+1)]

        for num,val in freq_map.items():
            bucket[val].append(num)

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result

