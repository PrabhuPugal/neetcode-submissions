class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter={}
        for i in range(len(nums)):
            if nums[i] in counter:
                return True
            else:
                counter[nums[i]]=True
        return False