class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements={}
        frequency=[[] for i in range(len(nums)+1)]

        for i in nums:
            elements[i]=elements.get(i,0)+1
        for i,j in elements.items():
            frequency[j].append(i)

        res=[]

        for x in range(len(frequency)-1,0,-1):
            for i in frequency[x]:
                res.append(i)
                if len(res)==k:
                    return res