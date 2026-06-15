class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count={}
        for i in strs:
            sorted_strs=''.join(sorted(i))
            if sorted_strs not in count:
                count[sorted_strs]=[i]
            else:
                count[sorted_strs].append(i)
        return list(count.values())